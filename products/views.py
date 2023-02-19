from django.shortcuts import render


def main_product_view(request):
    context = {}
    return render(request, "main_product.html", context)


def sub_product_view(request):
    context = {}
    return render(request, "sub_product.html", context)
