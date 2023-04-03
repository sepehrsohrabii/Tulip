from django.http import HttpResponseRedirect
from django.shortcuts import render

from emailMarketing.forms import ContactForm
from products.models import (
    MainProduct,
    MainProduct2,
    MainProductGallery,
    SubProduct,
    SubProductGallery,
)


def main_product_view(request, main_product_slug):
    try:
        main_product = MainProduct.objects.get(slug=main_product_slug)
    except MainProduct.DoesNotExist:
        main_product = None

    try:
        main_product2 = MainProduct2.objects.get(slug=main_product_slug)
    except MainProduct2.DoesNotExist:
        main_product2 = None

    try:
        sub_products = SubProduct.objects.filter(main_product=main_product)
    except SubProduct.DoesNotExist:
        sub_products = None

    context = {
        "main_product": main_product,
        "main_product2": main_product2,
        "sub_products": sub_products,
    }
    if main_product:
        context = {
            "main_product": main_product,
            "main_product2": main_product2,
            "sub_products": sub_products,
        }
        return render(request, "main_product.html", context)
    elif main_product2:
        gallery = MainProductGallery.objects.filter(main_product=main_product2)
        context = {
            "main_product": main_product,
            "main_product2": main_product2,
            "sub_products": sub_products,
            "gallery": gallery,
        }
        return render(request, "main_product2.html", context)


def sub_product_view(request, main_product_slug, sub_product_slug):
    main_product = MainProduct.objects.get(slug=main_product_slug)
    sub_product = SubProduct.objects.get(
        slug=sub_product_slug, main_product=main_product
    )
    gallery = SubProductGallery.objects.filter(sub_product=sub_product)
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
    context = {"form": form, "sub_product": sub_product, "gallery": gallery}
    return render(request, "sub_product.html", context)
