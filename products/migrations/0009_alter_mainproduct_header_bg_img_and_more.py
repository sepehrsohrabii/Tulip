# Generated by Django 4.1.5 on 2023-04-03 22:04

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_mainproduct2_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproduct',
            name='header_bg_img',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='mainproduct',
            name='product_img',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='mainproduct2',
            name='header_bg_img',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='mainproduct2',
            name='product_img',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='subproduct',
            name='header_bg_img',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path),
        ),
    ]
