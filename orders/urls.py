import orders
from .views import *
from django.urls import path




urlpatterns = [
path('checkout/', checkout, name='checkout'),
path('order_history/', order_history, name='order_history'),

]