from django.urls import path
from products.views import *

urlpatterns = [
    path('categories/', categories , name='categories'),
    path('products/', products , name='products'),
]