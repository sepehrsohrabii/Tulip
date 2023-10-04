from django.shortcuts import render

from blog.models import Blog
from frontend.models import Settings


def home_page(request):
    blogs = Blog.objects.filter(status=True).order_by("-create_at")[:3]
    setting, created = Settings.objects.get_or_create(is_active=True)
    context = {
        "setting": setting,
        "blogs": blogs,
    }
    return render(request, "home.html", context)


def about_us(request):
    context = {}
    return render(request, "about_us.html", context)


def coming_soon(request):
    context = {}
    return render(request, "coming_soon.html", context)
