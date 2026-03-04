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
    prioridade = models.CharField(max_length=10)

    def __str__(self):
        return self.nomeProjeto

class Tarefa(models.Model):
    nomeTarefa = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    dataInicio = models.DateField()
    dataFim = models.DateField()
    prioridade = models.CharField(max_length=10)
    etiqueta = models.CharField(max_length=30)

    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name="tarefas"
    )

    def __str__(self):
        return self.nomeTarefa
