from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.loginV, name='login'),
    path('logout/', views.deslogar, name='logout'),
    path('registro/', views.cadastrar, name='registro'),
    path("editar/", views.editar, name="editar"),
    path("projetos/", views.consultarProjeto, name="projetos"),
    path("kanban/<int:id>/", views.consultarTarefa, name="consultarTarefa"),
    path("projetos/criar/", views.cadastrarProjeto, name="cadastrarProjeto"),
    path("tarefa/adicionar/<int:id>/", views.cadastrarTarefa, name="cadastrarTarefa"),
    path("tarefa/mover/", views.moverTarefa, name="moverTarefa"),
]
