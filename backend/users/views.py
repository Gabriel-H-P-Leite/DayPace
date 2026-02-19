from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def registro_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe.")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
    
    return render(request, 'registro.html')
