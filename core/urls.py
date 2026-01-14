from django.contrib import admin
from django.urls import path, include
from home.views import *
from django.conf.urls.static import static
from core import settings

import users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('users/', include("users.urls")),
    path('catalog/', include("products.urls")),
    path('cart/', include("cart.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
