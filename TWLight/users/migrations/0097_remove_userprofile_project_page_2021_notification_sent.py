# Generated by Django 4.2.11 on 2024-06-25 01:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0096_remove_editor_occupation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="project_page_2021_notification_sent",
        ),
    ]
