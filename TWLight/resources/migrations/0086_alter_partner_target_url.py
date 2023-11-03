# Generated by Django 3.2.20 on 2023-09-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0085_alter_suggestion_suggested_company_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="target_url",
            field=models.URLField(
                blank=True,
                help_text="Link to partner resources. Required for proxied resources; optional otherwise.",
                null=True,
                unique=True,
            ),
        ),
    ]
