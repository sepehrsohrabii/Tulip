import os
import random

from django.db import models

from .validators import validate_file_extension


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
    return f"settings/{final_name}"


class Settings(models.Model):
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=50, blank=True)
    slider_video_url = models.URLField(max_length=200,
                                       verbose_name="Slider Video URL",
                                       blank=True)
    view_count = models.BigIntegerField(default=0, verbose_name="View Count")
    header_logo = models.FileField(
        upload_to=upload_image_path,
        validators=[validate_file_extension],
        verbose_name="Header Logo",
        blank=True,
    )
    footer_logo = models.FileField(
        upload_to=upload_image_path,
        validators=[validate_file_extension],
        verbose_name="Footer Logo",
        blank=True,
    )
    img_sec_one = models.ImageField(upload_to=upload_image_path,
                                    verbose_name="IMG Section one",
                                    blank=True)
    img_sec_two = models.ImageField(upload_to=upload_image_path,
                                    verbose_name="IMG Section two",
                                    blank=True)
    img_sec_three = models.ImageField(upload_to=upload_image_path,
                                      verbose_name="IMG Section three",
                                      blank=True)
    img_sec_four = models.ImageField(upload_to=upload_image_path,
                                     verbose_name="IMG Section four",
                                     blank=True)
    bottom_video_url = models.URLField(max_length=200,
                                       verbose_name="Bottom Video URL",
                                       blank=True)

    def save(self, *args, **kwargs):
        if self.is_active:
            # deactivate any other active instances
            Settings.objects.exclude(id=self.id).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.title, self.is_active)
