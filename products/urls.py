from django.urls import path
from products.views import *

urlpatterns = [
    path('categories/', categories , name='categories'),
    path('category/<slug:slug>', products_by_category, name='products_by_category'),
    path('search/', search, name='search'),
    path('product/<slug:slug>', product_detail, name='product_detail'),
]