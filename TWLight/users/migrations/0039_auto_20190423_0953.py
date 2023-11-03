# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-23 09:53


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("users", "0038_auto_20190220_1639")]

    operations = [
        migrations.AddField(
            model_name="authorization",
            name="reminder_email_sent",
            field=models.BooleanField(
                default=False,
                help_text="Have we sent a reminder email about this authorization?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="send_renewal_notices",
            field=models.BooleanField(
                default=True, help_text="Does this user want renewal reminder notices?"
            ),
        ),
    ]
