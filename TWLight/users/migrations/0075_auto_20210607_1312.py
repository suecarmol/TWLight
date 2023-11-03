# Generated by Django 3.1.8 on 2021-06-07 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0074_auto_20210603_1500"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="lang",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ar", "العربية"),
                    ("as", "অসমীয়া"),
                    ("bcl", "Bikol Central"),
                    ("br", "brezhoneg"),
                    ("da", "dansk"),
                    ("dag", "dagbanli"),
                    ("de", "Deutsch"),
                    ("diq", "Zazaki"),
                    ("en", "English"),
                    ("en-gb", "British English"),
                    ("eo", "Esperanto"),
                    ("es", "español"),
                    ("fa", "فارسی"),
                    ("fi", "suomi"),
                    ("fr", "français"),
                    ("gu", "ગુજરાતી"),
                    ("he", "עברית"),
                    ("hi", "हिन्दी"),
                    ("hy", "հայերեն"),
                    ("id", "Bahasa Indonesia"),
                    ("io", "Ido"),
                    ("it", "italiano"),
                    ("ja", "日本語"),
                    ("ko", "한국어"),
                    ("lv", "latviešu"),
                    ("mk", "македонски"),
                    ("mnw", "ဘာသာ မန်"),
                    ("mr", "मराठी"),
                    ("ms", "Bahasa Melayu"),
                    ("my", "မြန်မာဘာသာ"),
                    ("pl", "polski"),
                    ("pt", "português"),
                    ("pt-br", "português do Brasil"),
                    ("ro", "română"),
                    ("ru", "русский"),
                    ("scn", "sicilianu"),
                    ("sr-ec", "sr-cyrl"),
                    ("sv", "svenska"),
                    ("ta", "தமிழ்"),
                    ("tr", "Türkçe"),
                    ("uk", "українська"),
                    ("vi", "Tiếng Việt"),
                    ("zh-hans", "中文（简体）"),
                    ("zh-hant", "中文（繁體）"),
                ],
                help_text="Language",
                max_length=128,
                null=True,
            ),
        ),
    ]
