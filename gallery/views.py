from django.shortcuts import render

from gallery.models import Item


# Create your views here.
def gallery_view(request):
    gallery_items = Item.objects.filter(status="True")
    return render(request, "gallery.html", {"gallery_items": gallery_items})
