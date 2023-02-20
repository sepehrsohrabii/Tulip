from django.urls import path

from frontend import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("about-us/", views.about_us, name="about_us"),
]
