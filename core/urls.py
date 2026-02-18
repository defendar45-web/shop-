from django.contrib import admin
from django.urls import path, include
from home.views import *
from django.conf.urls.static import static
from core import settings

import users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),


    path('users/', include("users.urls")),
    path('catalog/', include("products.urls")),
    path('cart/', include("cart.urls")),
    path('orders/', include("orders.urls")),
    path('seminars/', include("courses.urls")),
    path('promo/', include("promotion.urls")),
    path('brands/' , include("brand.urls")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
