# Generated by Django 4.1.5 on 2023-04-02 10:34

import ckeditor.fields
from django.db import migrations, models

import products.models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_alter_mainproduct_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MainProduct2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("True", "Active"), ("False", "Not active")],
                        default="True",
                        max_length=50,
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("description", ckeditor.fields.RichTextField()),
                (
                    "slug",
                    models.SlugField(
                        allow_unicode=True,
                        max_length=200,
                        unique=True,
                        verbose_name="link",
                    ),
                ),
                (
                    "header_bg_img",
                    models.ImageField(
                        upload_to=products.models.upload_image_path),
                ),
                (
                    "product_img",
                    models.ImageField(
                        upload_to=products.models.upload_image_path),
                ),
                (
                    "create_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "view_count",
                    models.BigIntegerField(
                        default=0, verbose_name="View Count"),
                ),
            ],
        ),
    ]
