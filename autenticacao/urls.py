
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *


urlpatterns = [
    path('', views.index,name='index'),
    path('admin/', admin.site.urls),
    path('senhas/', include('senhas.urls'))
] 
