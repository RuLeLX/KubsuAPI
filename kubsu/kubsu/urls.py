from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', AuthUser, name='Authorization'),   #User start work there
    path('profile/', include('Account.urls'))

]
