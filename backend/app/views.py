import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EditarUsuarioForm
from .models import Projeto, Tarefa


def home(request):
    return render(request, 'home.html')

def cadastrar(request):
    #valores no form
    if request.method == "POST":
        campos = {
            'nome de usuário' : request.POST.get("nomeUsuario"),
            'email' : request.POST.get("email"),
            'nome' : request.POST.get("nome"),
            'sobrenome' : request.POST.get("sobrenome"),
            'senha' : request.POST.get("senha")
        }
        #remove espaços em branco e salva tudo em minusculo
        for chave, valor in campos.items():
            if chave != 'senha':
                campos[chave] = valor.strip().lower() if valor else valor
        #verifica se algum campo esta vazio
        for nomeCampo, valor in campos.items():
            if not valor:
                messages.error(request, f"O campo {nomeCampo} é obrigatório")
                return redirect("registro")
        if User.objects.filter(username=campos['nome de usuário']).exists():
            messages.error(request, "Usuário já existe")
            return redirect("registro")
        if User.objects.filter(email=campos['email']).exists():
            messages.error(request, "Email já cadastrado")
            return redirect("registro")
        #adiciona em user os valores
        user = User.objects.create_user(
        username=campos['nome de usuário'],
        email=campos['email'],
        first_name=campos['nome'],
        last_name=campos['sobrenome'],
        password=campos['senha']
        )
        return redirect("login")
    return render(request, "registro.html")

@login_required
def editar(request):
    form = EditarUsuarioForm(
        request.POST or None,
        instance=request.user
    )
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "editar.html", {"form": form})

def loginV(request):
    if request.method == "POST":
        username =  request.POST.get("nomeUsuario").strip().lower()
        password = request.POST.get("senha").strip().lower()
        user = authenticate(request, username=username, password=password)
        #se user não for "" NULL
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'login.html')

def deslogar(request):
    logout(request)
    return redirect('home')

def recuperarSenha(request):
    logout(request)
    return redirect('home')

#PROJETOS
@login_required
def cadastrarProjeto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        if not nome or nome.strip() == "":
            messages.error(request, "Nome não pode ser vazio")
        else:
            Projeto.objects.create(
                user=request.user,
                nomeProjeto=nome.strip(),
            )
        return redirect("projetos")

    return render(request, "projetos.html")

@login_required
def editarProjeto(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        prioridade = request.POST.get("prioridade")

        projeto = get_object_or_404(Projeto, id=id)
        projeto.nomeProjeto = nome

        if prioridade is None or prioridade == "":
            projeto.prioridade = None
        else:
            projeto.prioridade = int(prioridade)
        if not nome or nome.strip() == "":
            messages.error(request, "Nome não pode ser vazio")
        else:
            projeto.save()
    return redirect("projetos")

@login_required
def excluirProjeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    projeto.delete()
    return redirect("projetos")

@login_required
def consultarProjeto(request):
    projetos = Projeto.objects.filter(user=request.user)
    return render(request, "projetos.html", {"projetos": projetos})

#TAREFAS
@login_required
def cadastrarTarefa(request, id):
    if request.method == "POST":
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        projeto = Projeto.objects.get(id=id)

        if not nome or nome.strip() == "":
            messages.error(request, "Nome não pode ser vazio")
        else:
            Tarefa.objects.create(
                nomeTarefa=nome,
                descricao=descricao,
                status="todo",
                projeto=projeto
            )
    return redirect("consultarTarefa", id=id)

@login_required
def editarTarefa(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        tarefa = get_object_or_404(Tarefa, id=id)

        tarefa.nomeTarefa = nome
        tarefa.descricao = descricao
        
        nome = request.POST.get("nome")
        if not nome or nome.strip() == "":
            messages.error(request, "Nome não pode ser vazio")
        else:
            tarefa.save()
    return redirect("consultarTarefa", id=tarefa.projeto.id)

@login_required
def excluirTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect("consultarTarefa", tarefa.projeto.id)

@login_required
def consultarTarefa(request, id):
    projeto = Projeto.objects.get(id=id)
    tarefas = Tarefa.objects.filter(projeto=projeto)

    todo = Tarefa.objects.filter(
        projeto=projeto,
        status="todo"
    ).order_by("prioridade")

    doing = Tarefa.objects.filter(
        projeto=projeto,
        status="doing"
    ).order_by("prioridade")

    done = Tarefa.objects.filter(
        projeto=projeto,
        status="done"
    ).order_by("prioridade")

    return render(request, "kanban.html", {
        "projeto": projeto,
        "tarefas": tarefas,
        "todo": todo,
        "doing": doing,
        "done": done
    })

@login_required
def moverTarefa(request):
    data = json.loads(request.body)

    tarefa = Tarefa.objects.get(id=data["id"])

    tarefa.status = data["status"]
    tarefa.save()

    return JsonResponse({"ok": True})

@login_required
def ordenarTarefas(request):

    data = json.loads(request.body)

    for item in data:

        tarefa = Tarefa.objects.get(id=item["id"])
        tarefa.prioridade = item["prioridade"]
        tarefa.status = item["status"]
        tarefa.save()

    return JsonResponse({"status":"ok"})
