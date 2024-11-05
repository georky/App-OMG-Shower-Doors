# productos/urls.py
from django.urls import path
from .views import create_product, product_list
urlpatterns = [
     path('products/new-product/', create_product, name='create_product'),
     path('products/product_list/', product_list, name='product_list'),
] 
