from django.urls import path

from products import views

urlpatterns = [
    path("<main_product_slug>/", views.main_product_view, name="main_product_view"),
    path(
        "<main_product_slug>/<sub_product_slug>/",
        views.sub_product_view,
        name="sub_product_view",
    ),
]
