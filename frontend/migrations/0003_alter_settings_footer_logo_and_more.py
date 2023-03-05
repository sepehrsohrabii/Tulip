# Generated by Django 4.1.5 on 2023-03-04 19:13

from django.db import migrations, models
import frontend.models
import frontend.validators


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_settings_bottom_video_url_settings_footer_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='footer_logo',
            field=models.ImageField(blank=True, upload_to=frontend.models.upload_image_path, validators=[frontend.validators.validate_file_extension], verbose_name='Footer Logo'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='header_logo',
            field=models.ImageField(blank=True, upload_to=frontend.models.upload_image_path, validators=[frontend.validators.validate_file_extension], verbose_name='Header Logo'),
        ),
    ]
