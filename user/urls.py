from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('logado/', views.logado, name='logado'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
]
