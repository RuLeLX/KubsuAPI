from django.urls import path, include
from .views import *

urlpatterns = [
    path('', UserData, name='Profile')
]