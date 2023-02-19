from django import forms
from django.forms import ModelForm

from emailMarketing.models import ContactFormModel, Subscription


class ContactForm(ModelForm):

    class Meta:
        model = ContactFormModel
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "message",
        )
        widgets = {
            "first_name":
            forms.TextInput(attrs={"placeholder": "Sepehr"}),
            "last_name":
            forms.TextInput(attrs={"placeholder": "Sohrabi"}),
            "email":
            forms.TextInput(attrs={"placeholder": "Enter your email here"}),
            "phone_number":
            forms.TextInput(
                attrs={"placeholder": "Enter your phone number here"}),
        }
        labels = {
            "first_name": ("First name"),
            "last_name": ("Last name"),
            "email": ("Email address"),
            "phone_number": ("Phone"),
            "message": ("Message"),
        }
        help_texts = {
            "message": ("Whe are here to help you ..."),
        }


class SubscriptionForm(ModelForm):

    class Meta:
        model = Subscription
        fields = ("email", )
        widgets = {
            "email":
            forms.TextInput(attrs={"placeholder": "Enter your email here"}),
        }
        labels = {
            "email": ("Email address"),
        }
