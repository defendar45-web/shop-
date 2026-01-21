
from .views import *
from django.urls import path




urlpatterns = [
path('checkout/', checkout, name='checkout'),
]