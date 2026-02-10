from django.urls import path
from promotion.views import *


urlpatterns = [
    path('',promotion, name='promotion'),

]