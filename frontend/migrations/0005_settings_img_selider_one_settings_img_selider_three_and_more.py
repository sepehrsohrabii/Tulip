# Generated by Django 4.1.5 on 2023-03-19 20:08

from django.db import migrations, models

import frontend.models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0004_alter_settings_footer_logo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="settings",
            name="img_selider_one",
            field=models.ImageField(
                blank=True,
                upload_to=frontend.models.upload_image_path,
                verbose_name="IMG Slider one",
            ),
        ),
        migrations.AddField(
            model_name="settings",
            name="img_selider_three",
            field=models.ImageField(
                blank=True,
                upload_to=frontend.models.upload_image_path,
                verbose_name="IMG Slider three",
            ),
        ),
        migrations.AddField(
            model_name="settings",
            name="img_selider_two",
            field=models.ImageField(
                blank=True,
                upload_to=frontend.models.upload_image_path,
                verbose_name="IMG Slider two",
            ),
        ),
    ]
