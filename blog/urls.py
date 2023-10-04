from django.urls import path

from blog import views

urlpatterns = [
    path("<slug>/", views.blog_view, name="blog_view"),
]
