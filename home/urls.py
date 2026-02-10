from .views import *
from django.urls import path

urlpatterns = [
path('', home, name='home'),
path('contact/', contact, name='contact'),
path('news/', news, name='news'),


]