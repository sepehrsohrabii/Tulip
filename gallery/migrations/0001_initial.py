# Generated by Django 4.1.5 on 2023-10-03 17:29

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('True', 'Active'), ('False', 'Not active')], default='True', max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=gallery.models.upload_image_path, verbose_name='Picture File')),
                ('video_url', models.URLField(blank=True, verbose_name='Video URL')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
            ],
        ),
    ]