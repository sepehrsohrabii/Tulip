import os
import random

from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


# for uploading pictures and creating it url
def upload_image_path(instance, filename):
    new_id = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    try:
        final_name = f"{new_id}-{instance.title}{ext}"
    except instance.title.DoesNotExist:
        final_name = f"{new_id}-{ext}"
    return f"products/{final_name}"


class MainProduct(models.Model):
    STATUS = (
        ("True", "Active"),
        ("False", "Not active"),
    )
    status = models.CharField(max_length=50, choices=STATUS, default="True")
    title = models.CharField(max_length=50)
    description = models.TextField(default="")
    slug = models.SlugField(verbose_name="link",
                            unique=True,
                            allow_unicode=True,
                            max_length=200)
    header_bg_img = models.ImageField(upload_to=upload_image_path,
                                      null=True,
                                      blank=True)
    product_img = models.ImageField(upload_to=upload_image_path,
                                    null=True,
                                    blank=True)
    create_at = models.DateTimeField(auto_now=True, verbose_name="Created at")
    view_count = models.BigIntegerField(default=0, verbose_name="View Count")

    def get_absolute_url(self):
        return reverse("main_product_view",
                       kwargs={"main_product_slug": self.slug})

    def __str__(self):
        return "{}-{}".format(self.title, self.create_at)


class MainProduct2(models.Model):
    STATUS = (
        ("True", "Active"),
        ("False", "Not active"),
    )
    status = models.CharField(max_length=50, choices=STATUS, default="True")
    title = models.CharField(max_length=50)
    short_description = models.TextField(default="")
    description = RichTextField()
    slug = models.SlugField(verbose_name="link",
                            unique=True,
                            allow_unicode=True,
                            max_length=200)
    header_bg_img = models.ImageField(upload_to=upload_image_path,
                                      null=True,
                                      blank=True)
    product_img = models.ImageField(upload_to=upload_image_path,
                                    null=True,
                                    blank=True)
    create_at = models.DateTimeField(auto_now=True, verbose_name="Created at")
    view_count = models.BigIntegerField(default=0, verbose_name="View Count")

    def get_absolute_url(self):
        return reverse("main_product_view",
                       kwargs={"main_product_slug": self.slug})

    def __str__(self):
        return "{}-{}".format(self.title, self.create_at)


class SubProduct(models.Model):
    STATUS = (
        ("True", "Active"),
        ("False", "Not active"),
    )
    status = models.CharField(max_length=50, choices=STATUS, default="True")
    main_product = models.ForeignKey(MainProduct,
                                     default=None,
                                     on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    short_description = models.TextField(default="")
    description = RichTextField()
    slug = models.SlugField(verbose_name="link",
                            unique=True,
                            allow_unicode=True,
                            max_length=200)
    title_img = models.ImageField(upload_to=upload_image_path)
    header_bg_img = models.ImageField(upload_to=upload_image_path,
                                      null=True,
                                      blank=True)
    header_img = models.ImageField(upload_to=upload_image_path)
    create_at = models.DateTimeField(auto_now=True, verbose_name="Created at")
    view_count = models.BigIntegerField(default=0, verbose_name="View Count")

    def get_absolute_url(self):
        return reverse(
            "sub_product_view",
            kwargs={
                "sub_product_slug": self.slug,
                "main_product_slug": self.main_product.slug,
            },
        )

    def __str__(self):
        return "{}-{}".format(self.title, self.create_at)


class SubProductGallery(models.Model):
    title = models.CharField(max_length=50)
    sub_product = models.ForeignKey(SubProduct,
                                    default=None,
                                    related_name="images",
                                    on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image_path, blank=True)


class MainProductGallery(models.Model):
    title = models.CharField(max_length=50)
    main_product = models.ForeignKey(
        MainProduct2,
        default=None,
        related_name="images",
        on_delete=models.CASCADE,
        null=True,
    )
    image = models.ImageField(upload_to=upload_image_path, blank=True)
