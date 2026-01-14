
from django.urls import path
from cart.views import *

urlpatterns = [
    path('', cart, name='cart'),
]