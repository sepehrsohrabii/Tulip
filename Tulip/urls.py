from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("frontend.urls")),
        path("products/", include("products.urls")),
        path("", include("emailMarketing.urls")),
        path("gallery/", include("gallery.urls")),
        path("blog/", include("blog.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
