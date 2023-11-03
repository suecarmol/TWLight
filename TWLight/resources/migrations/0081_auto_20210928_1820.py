# Generated by Django 3.1.13 on 2021-09-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0079_remove_authorization_stream"),
        ("applications", "0003_remove_application_specific_stream"),
        ("resources", "0080_auto_20210907_1415"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="partner",
            name="mutually_exclusive",
        ),
        migrations.RemoveField(
            model_name="partner",
            name="specific_stream",
        ),
        migrations.AlterField(
            model_name="partner",
            name="accounts_available",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Add the number of new accounts to the existing value, not by resetting it to zero.",
                null=True,
            ),
        ),
        migrations.DeleteModel(
            name="Stream",
        ),
    ]
