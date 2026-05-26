from django.utils import timezone
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Projeto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projetos")
    nomeProjeto = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    dataInicio = models.DateField(default=timezone.now)
    dataFim = models.DateField(null=True, blank=True)
    prioridade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nomeProjeto

class Tarefa(models.Model):
    STATUS = [
        ("todo", "A Fazer"),
        ("doing", "Fazendo"),
        ("done", "Concluído"),
    ]
    nomeTarefa = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    status = models.CharField(max_length=10,choices=STATUS,default="todo")
    dataInicio = models.DateField(default=timezone.now)
    dataFim = models.DateField(null=True, blank=True)
    prioridade = models.IntegerField(default=0)
    etiqueta = models.CharField(max_length=30)
    class Meta:
        ordering = ['-prioridade']
    
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )
    def __str__(self):
        return self.nomeTarefa
