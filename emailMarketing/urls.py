from django.urls import path

from emailMarketing import views

urlpatterns = [
    path("contact-us/", views.contact_page, name="contact_page"),
]
