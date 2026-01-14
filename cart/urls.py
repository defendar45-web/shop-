
from django.urls import path
from cart.views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
]