from django.shortcuts import render


def home_page(request):
    context = {

    }
    return render(request, 'home.html', context)


def contact_us(request):
    context = {

    }
    return render(request, 'contact_us.html', context)


def about_us(request):
    context = {

    }
    return render(request, 'about_us.html', context)
