from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254, help_text='O Email precisa ser válido.')

    class Meta:
        model = CustomUser
        fields = ('nome','username','email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password']