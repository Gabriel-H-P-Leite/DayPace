from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Projeto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EditarUsuarioForm

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

        if nome:
            Projeto.objects.create(
                user=request.user,
                nomeProjeto=nome.strip(),
               
            )
            return redirect("projetos")

    return render(request, "cadastrar_projeto.html")

@login_required
def consultarProjeto(request):
    projetos = Projeto.objects.filter(user=request.user)
    return render(request, "projetos.html", {"projetos": projetos})

@login_required
def quadro(request, id):
    projeto = Projeto.objects.get(id=id, user=request.user)
    return render(request, "kanban.html", {"projeto": projeto})
from django.shortcuts import redirect
