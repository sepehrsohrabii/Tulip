from django.shortcuts import render

from emailMarketing.forms import ContactForm
from emailMarketing.models import ContactFormModel


def contact_page(request):
    form = ContactForm(request.POST, auto_id=True)

    contact = []

    if request.method == "POST":
        if form.is_valid():
            contact_save = ContactFormModel()
            form = ContactForm(request.POST,
                               instance=contact_save,
                               auto_id=True)
            contact = form.save(commit=False)
            contact.save()
    else:
        form = ContactForm()

    return render(
        request,
        "contact_us.html",
        {
            "form": form,
        },
    )
