from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=50, required=True,
    label="Nombre de usuario",
    error_messages = {'required': 'El usuario es obligatorio'})
    password = forms.CharField(widget = forms.PasswordInput, max_length=20,
    label="Contraseña", required=True, error_messages={'required': 'La contraseña es obligatoria'})

