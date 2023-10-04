import os
import random

from django.db import models


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
    return f"gallery/{final_name}"


class Item(models.Model):
    STATUS = (
        ("True", "Active"),
        ("False", "Not active"),
    )
    status = models.CharField(max_length=50, choices=STATUS, default="True")
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to=upload_image_path,
                                verbose_name="Picture File",
                                null=True,
                                blank=True)
    video_url = models.URLField(max_length=200,
                                verbose_name="Video URL",
                                blank=True)
    create_at = models.DateTimeField(auto_now=True, verbose_name="Created at")

    def __str__(self):
        return "{}-{}".format(self.title, self.create_at)
