from django.urls import path
from . import views

urlpatterns = [
    
    
    path('criar/', views.criar,name='criar'),
    path('toke/<int:id>',views.toke,name='toke'),
    path('ir/',views.ir,name='ir'),
    path('login/',views.login,name='login'),
    path('ir_login/',views.ir_login,name='ir_login'),
    path('ir_muda/',views.ir_muda,name='ir_muda'),
    path('mudar/',views.mudar,name='mudar'),
    path('logout/',views.logout,name='logout')
    
   
]