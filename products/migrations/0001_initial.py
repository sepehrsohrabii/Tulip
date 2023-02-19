# Generated by Django 4.1.5 on 2023-02-12 22:14

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models

import products.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MainProduct",
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
                ("description", models.TextField(blank=True, null=True)),
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
                        blank=True,
                        null=True,
                        upload_to=products.models.upload_image_path,
                    ),
                ),
                (
                    "product_img",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=products.models.upload_image_path,
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True,
                                         verbose_name="Created at"),
                ),
                (
                    "view_count",
                    models.BigIntegerField(default=0,
                                           verbose_name="View Count"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SubProduct",
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
                    "header_img",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=products.models.upload_image_path,
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True,
                                         verbose_name="Created at"),
                ),
                (
                    "view_count",
                    models.BigIntegerField(default=0,
                                           verbose_name="View Count"),
                ),
                (
                    "main_product",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.mainproduct",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Images",
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
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to=products.models.upload_image_path),
                ),
                (
                    "sub_product",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="products.subproduct",
                    ),
                ),
            ],
        ),
    ]
