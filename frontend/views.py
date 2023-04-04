from django.shortcuts import render

from frontend.models import Settings


def home_page(request):
    setting, created = Settings.objects.get_or_create(is_active=True)
    context = {"setting": setting}
    return render(request, "home.html", context)


def about_us(request):
    context = {}
    return render(request, "about_us.html", context)


def coming_soon(request):
    context = {}
    return render(request, "coming_soon.html", context)
