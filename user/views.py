from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm
from .utils import verifica_autenticacao

def cadastrar_usuario(request):
    if verifica_autenticacao(request):
        # Se o usuário já estiver autenticado, redirecione para a página logado
        return redirect('logado')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('logado')
    else:
        form = CustomUserCreationForm()

    return render(request, 'user/cadastrar_usuario.html', {'form': form})

def logado(request):
    return render(request, 'user/logado.html', {'user': request.user})

def login_view(request):
    if verifica_autenticacao(request):
        return redirect('logado')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('logado')
    else:
        form = AuthenticationForm()

    return render(request, 'user/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('index')
