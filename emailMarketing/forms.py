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
            forms.TextInput(attrs={"placeholder": "Enter your first name"}),
            "last_name":
            forms.TextInput(attrs={"placeholder": "Enter your last name"}),
            "email":
            forms.TextInput(attrs={"placeholder": "Enter your email here"}),
            "phone_number":
            forms.TextInput(
                attrs={"placeholder": "Enter your phone number here"}),
            "message":
            forms.TextInput(
                attrs={"placeholder": "Whe are here to help you ..."}),
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

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "input-1 mt-2 w-100"


class SubscriptionForm(ModelForm):

    class Meta:
        model = Subscription
        fields = ("email", )
        widgets = {
            "email": forms.TextInput(attrs={"placeholder": "Email address"}),
        }
        labels = {
            "email": ("Email address"),
        }

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "input-1"
