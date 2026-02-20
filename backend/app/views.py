from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

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

def deslogar(request):
    logout(request)
    return redirect('home')

def loginV(request):
    if request.method == "POST":
        username =  request.POST.get("nomeUsuario")
        password = request.POST.get("senha")
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
