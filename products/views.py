from django.http import HttpResponseRedirect
from django.shortcuts import render

from emailMarketing.forms import ContactForm
from products.models import MainProduct, SubProduct


def main_product_view(request, slug):
    main_product = MainProduct.objects.get(slug=slug)
    sub_products = SubProduct.objects.filter(main_product=main_product)
    context = {"main_product": main_product, "sub_products": sub_products}
    return render(request, "main_product.html", context)


def sub_product_view(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

        # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    context = {
        "form": form,
    }
    return render(request, "sub_product.html", context)
