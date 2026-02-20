from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.loginV, name='login'),
    path('logout/', views.deslogar, name='logout'),
    path('registro/', views.cadastrar, name='registro'),
]
