import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EditarUsuarioForm
from .models import Projeto, Tarefa, Perfil


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
            'senha' : request.POST.get("senha"),
            'telefone' : request.POST.get("telefone")
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
        if Perfil.objects.filter(telefone=campos['telefone']).exists():
            messages.error(request, "Telefone já cadastrado")
            return redirect("registro")
        Perfil.objects.create(user=user, telefone=campos.get('telefone', ''))
        return redirect("login")
    return render(request, "registro.html")

@login_required
def editar(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    form = EditarUsuarioForm( request.POST or None, instance=request.user)

    if request.method == "POST" and form.is_valid():
        form.save()
        perfil.telefone = request.POST.get("telefone", "")
        perfil.save()

        senha = request.POST.get("senha")
        confirmarSenha = request.POST.get("confirmarSenha")
        if senha:
            if senha == confirmarSenha:
                request.user.set_password(senha)
                request.user.save()
                login(request, request.user)  # mantém o usuário logado após mudar senha
            else:
                messages.error(request, "As senhas não coincidem")
                return redirect("editar")
    return render(request, "editar.html", {"form": form, "perfil": perfil})

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
        descricao = request.POST.get("descricao")
        if not nome or nome.strip() == "":
            messages.error(request, "Nome não pode ser vazio")
        else:
            Projeto.objects.create(
                user=request.user,
                nomeProjeto=nome.strip(),
                descricao=descricao,
                prioridade = 0
            )
        return redirect("projetos")

    return render(request, "projetos.html")

@login_required
def editarProjeto(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        projeto = get_object_or_404(Projeto, id=id)
        prioridade = request.POST.get("prioridade")
        descricao = request.POST.get("descricao")
        dataInicio = request.POST.get("dataInicio") or None
        dataFim = request.POST.get("dataFim") or None
        prioridade = int(request.POST.get("prioridade"))
        quantidade = Projeto.objects.filter(user=request.user).count()

        projeto.nomeProjeto = nome
        projeto.descricao = descricao
        projeto.dataInicio = dataInicio
        projeto.dataFim = dataFim

        if prioridade > quantidade:
            projeto.prioridade = quantidade
        else:
            projeto.prioridade = int(prioridade)

        #testa nome vazio
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
        dataInicio = request.POST.get("dataInicio") or None
        dataFim = request.POST.get("dataFim") or None
        tarefa = get_object_or_404(Tarefa, id=id)
        prioridade = int(request.POST.get("prioridade"))
        quantidade = Tarefa.objects.filter(
            projeto=tarefa.projeto
        ).count()

        if prioridade > quantidade:
            tarefa.prioridade = quantidade
        else:
            tarefa.prioridade = prioridade
        tarefa.nomeTarefa = nome
        tarefa.descricao = descricao
        tarefa.dataInicio = dataInicio
        tarefa.dataFim = dataFim
        
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
    )
    doing = Tarefa.objects.filter(
        projeto=projeto,
        status="doing"
    )
    done = Tarefa.objects.filter(
        projeto=projeto,
        status="done"
    )
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
