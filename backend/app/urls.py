from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.loginV, name='login'),
    path('logout/', views.deslogar, name='logout'),
    path('registro/', views.cadastrar, name='registro'),
    path("editar/", views.editar, name="editar"),
    path("projetos/", views.consultarProjeto, name="projetos"),
    path("kanban/<int:id>/", views.quadro, name="quadro"),
    path("projetos/criar/", views.cadastrarProjeto, name="cadastrarProjeto"),
]
