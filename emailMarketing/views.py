from django.shortcuts import render

from emailMarketing.forms import ContactForm
from emailMarketing.models import ContactFormModel


def contact_page(request):
    contact_form = ContactForm(request.POST, auto_id=True)

    contact = []

    if request.method == "POST":
        if contact_form.is_valid():
            contact_save = ContactFormModel()
            contact_form = ContactForm(request.POST,
                                       instance=contact_save,
                                       auto_id=True)
            contact = contact_form.save(commit=False)
            contact.save()

    return render(
        request,
        "contact-us.html",
        {
            "contact_form": contact_form,
        },
    )
