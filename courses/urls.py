from django.urls import path
from courses.views import *


urlpatterns = [
    path('', seminars, name='seminars'),
    path('<int:id>/', seminar_detail, name='seminar_detail'),
]