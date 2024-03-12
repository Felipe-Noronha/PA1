from django.shortcuts import redirect
from django.urls import reverse

def verifica_autenticacao(request):
    if request.user.is_authenticated:
        return True
    else:
        # Se o usuário não estiver autenticado, redirecione para a página de login
        return False
