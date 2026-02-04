from django.urls import path
from users.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/', profile, name='profile'),
    path('auth_logout/', auth_logout, name='auth_logout')
] 