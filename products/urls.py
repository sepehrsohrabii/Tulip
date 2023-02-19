from django.urls import path

from products import views

urlpatterns = [
    # path('<slug>/', views.main_product_view, name='main_product_view'),
    path('test/', views.main_product_view, name='main_product_view'),
    path('test2/', views.sub_product_view, name='sub_product_view'),
]
