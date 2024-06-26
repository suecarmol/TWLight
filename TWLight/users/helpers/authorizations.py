from django.db.models import QuerySet

from TWLight.resources.models import Partner
from TWLight.users.models import Authorization


def get_all_bundle_authorizations():
    """
    Returns all Bundle authorizations, both active
    and not.

    Returns
    -------
    QuerySet
    """

    # distinct() required because partners__authorization_method is ManyToMany
    return (
        Authorization.objects.select_for_update()
        .filter(partners__authorization_method=Partner.BUNDLE)
        .distinct()
    )


def create_resource_dict(authorization: Authorization, partner: Partner):
    """
    For a given authorization and associated partner, fetch some additional
    information for use in sort_authorizations_into_resource_list().

    Parameters
    ----------
    authorization: Authorization
        An Authorization object.
    partner: Partner
        A Partner object linked to this Authorization object.
    Returns
    -------
    dict
    """
    resource_item = {
        "partner": partner,
        "authorization": authorization,
    }

    access_url = partner.get_access_url
    resource_item["access_url"] = access_url

    valid_authorization = authorization.is_valid
    resource_item["valid_proxy_authorization"] = (
        partner.authorization_method == partner.PROXY and valid_authorization
    )
    resource_item["valid_authorization_with_access_url"] = (
        access_url
        and valid_authorization
        and authorization.user.userprofile.terms_of_use
    )

    return resource_item


def delete_duplicate_bundle_authorizations(authorizations: QuerySet):
    """
    Given a queryset of Authorization objects, find the ones which are
    Bundle authorizations, then locate and delete any duplicates for
    each user.

    Parameters
    ----------
    authorizations: QuerySet
        Queryset of Authorization objects to check for duplicates.
    """
    bundle_authorizations = authorizations.filter(
        partners__authorization_method=Partner.BUNDLE
    )
    # Get a list of users with bundle auths
    for user_id in bundle_authorizations.values_list("user_id"):
        # get the distinct set of authorizations for the user
        user_authorizations = bundle_authorizations.filter(user_id=user_id).distinct()
        # There should be no more than one bundle auth per user, so slice the queryest to get any auths beyond that
        for duplicate_authorization in user_authorizations[1:].iterator():
            # Delete it
            duplicate_authorization.delete()


def sort_authorizations_into_resource_list(authorizations: QuerySet):
    """
    Given a queryset of Authorization objects, return a
    list of dictionaries, sorted alphabetically by partner
    name, with additional data computed for ease of display
    in the my_library template.

    Parameters
    ----------
    authorizations: QuerySet
        Queryset of Authorization objects
    """
    resource_list = []
    if authorizations:
        for authorization in authorizations:
            for partner in authorization.partners.all():
                resource_list.append(create_resource_dict(authorization, partner))

        # Alphabetise by name
        resource_list = sorted(
            resource_list, key=lambda i: i["partner"].company_name.lower()
        )

        return resource_list
    else:
        return None
