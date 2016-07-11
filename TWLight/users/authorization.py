# Authorization views...

# Log in...
# handshaker.initiate
# save request_token in the session or somewhere
# and then return a redirect to the mediawiki URL

# they will be redirected back to my callback with a response token
# callback view needs to parse the response token
# and then use it and the request token to handshaker.complete() and get an
# access token
# I can use the access token to get identify() info

# do I want/need to save the access token? Do I want to make sure to
# periodically update people's wikipedia information, not just when they log in?

import logging
from mwoauth import ConsumerToken, Handshaker, AccessToken

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.utils.translation import ugettext as _

from .models import Editor


logger = logging.getLogger(__name__)

# Construct a "consumer" from the key/secret provided by MediaWiki
consumer_token = ConsumerToken(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)

# Construct handshaker with wiki URI and consumer
handshaker = Handshaker(settings.WP_OAUTH_BASE_URL, consumer_token)


def dehydrate_token(token):
    """
    Convert the request token into a dict suitable for storing in the session.
    """
    session_token = {}
    session_token['key'] = token.key
    session_token['secret'] = token.secret
    return session_token


def rehydrate_token(token):
    """
    Convert the stored dict back into a request token that we can use for
    getting an access grant.
    """
    request_token = ConsumerToken(token['key'], token['secret'])
    return request_token


class OAuthBackend(object):

    def _create_user_and_editor(self, identity):
        logger.info('creating user')

        # -------------------------- Create the user ---------------------------
        email = identity['email']
        username = identity['sub']

        # Since we are not providing a password argument, this will call
        # set_unusable_password, which is exactly what we want; users created
        # via OAuth should only be allowed to log in via OAuth.
        user = User.objects.create_user(username=username, email=email)

        # ------------------------- Create the editor --------------------------
        editor = Editor()

        editor.user = user
        editor.wp_sub = identity['sub']
        editor.update_from_wikipedia(identity) # This call also saves the editor

        return user, editor


    def _get_and_update_user_from_identity(self, identity):
        """
        If we have an Editor matching the identity returned by Wikipedia,
        update it with the identity parameters and return its associated user.
        If we don't, create an Editor and User, and return that user.
        Also return a boolean that is True if we created a user during this
        call and False if we did not.
        """
        logger.info('getting user')
        try:
            editor = Editor.objects.get(wp_sub=identity['sub'])
            user = editor.user
            created = False
        except Editor.DoesNotExist:
            user, editor = self._create_user_and_editor(identity)
            created = True

        editor.update_from_wikipedia(identity)

        return user, created


    def authenticate(self, request=None, access_token=None):
        if not request or not access_token:
            # You must have meant to use a different authentication backend.
            # Returning None will make Django keep going down its list of
            # options.
            return None

        try:
            assert isinstance(access_token, AccessToken)
        except AssertionError:
            return None

        # Get identifying information about the user. This doubles as a way
        # to authenticate the access token, which only Wikimedia can do,
        # and thereby to authenticate the user (which is hard for us to do as
        # we have no password.)
        try:
            identity = handshaker.identify(access_token)
        except:
            logger.warning('Someone tried to log in but presented an invalid '
                'access token')
            raise PermissionDenied

        logger.info('identity was %s', identity)

        # Get or create the user.
        user, created = self._get_and_update_user_from_identity(identity)
        request.session['user_created'] = created

        # The authenticate() function of a Django auth backend must return
        # the user.
        return user


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



class OAuthInitializeView(View):
    """
    Ask Wikipedia for a temporary key/secret for the user, and redirect
    them to Wikipedia to confirm authorization.
    """

    def get(self, request, *args, **kwargs):
        redirect, request_token = handshaker.initiate()
        request.session['request_token'] = dehydrate_token(request_token)
        # TODO where is the proper, secure place to store this?
        logger.info('request token was %s', request_token)
        return HttpResponseRedirect(redirect)



class OAuthCallbackView(View):
    """
    Receive the redirect from Wikipedia and parse the response token.
    """

    def get(self, request, *args, **kwargs):
        response_qs = request.META['QUERY_STRING']
        logger.info('response querystring was %s', response_qs)
        session_token = request.session.pop('request_token', None)
        request_token = rehydrate_token(session_token)

        logger.info('request token was %s', request_token)
        if not request_token:
            logger.info('no request token :(')
            raise PermissionDenied

        try:
            access_token = handshaker.complete(request_token, response_qs)
            logger.info('access token was %s', access_token)
        except:
            logger.info('no access token :(')
            raise PermissionDenied

        user = authenticate(request=request, access_token=access_token)
        login(request, user)

        created = request.session.pop('user_created', False)

        if created:
            # Translators: this message is displayed to users with brand new accounts.
            messages.add_message(request, messages.INFO, _('Welcome! Please '
                'agree to the terms of use.'))
            url = reverse_lazy('terms')
        else:
            messages.add_message(request, messages.INFO, _('Welcome back!'))
            url = reverse_lazy('users:editor_detail',
                kwargs={'pk': user.editor.pk})

        return HttpResponseRedirect(url)
