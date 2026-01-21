
from django.urls import path
from cart.views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('<str:action>/change/quantity/<int:item_id>/', change_quantity, name='change_quantity'),
]