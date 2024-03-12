from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
]