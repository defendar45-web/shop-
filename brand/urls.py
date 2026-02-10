from django.urls import path

from brand.views import *

urlpatterns = [
    path('', brands , name='brands'),
]