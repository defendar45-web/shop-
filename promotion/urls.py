from django.urls import path

from promotion.models import promo_image
from promotion.views import *


urlpatterns = [
    path('',promotion, name='promotion'),
    path('<int:promo_id>/', promo_image, name='promo_image'),

]