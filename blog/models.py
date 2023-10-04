import os
import random
from django.db import models
from ckeditor.fields import RichTextField
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
    return f"blog/{final_name}"


class Blog(models.Model):
    STATUS = (
        ("True", "Active"),
        ("False", "Not active"),
    )
    status = models.CharField(max_length=50, choices=STATUS, default="True")
    slug = models.SlugField(
        verbose_name="link", unique=True, allow_unicode=True, max_length=200
    )
    title = models.CharField(max_length=50)
    short_description = models.TextField(default="")
    description = RichTextField()

    img = models.ImageField(upload_to=upload_image_path)
    create_at = models.DateTimeField(auto_now=True, verbose_name="Created at")

    def get_absolute_url(self):
        return reverse("blog_view", kwargs={"slug": self.slug})

    def __str__(self):
        return "{}-{}".format(self.title, self.create_at)
