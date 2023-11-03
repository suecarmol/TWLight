# Generated by Django 3.0.11 on 2020-11-20 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0064_auto_20201019_1310"),
    ]

    operations = [
        migrations.CreateModel(
            name="EditorLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "editcount",
                    models.IntegerField(
                        default=None, editable=False, help_text="Wikipedia edit count"
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        db_index=True,
                        default=None,
                        editable=False,
                        help_text="When the editcount was updated from Wikipedia",
                    ),
                ),
                (
                    "editor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="editorlogs",
                        to="users.Editor",
                    ),
                ),
            ],
        ),
    ]
