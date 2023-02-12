from django.db import models


class ContactFormModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.TextField()


class Subscription(models.Model):
    email = models.CharField(max_length=255)
