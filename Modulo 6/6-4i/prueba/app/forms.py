from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput)
    group = forms.ModelChoiceField(queryset=Group.objects.all())
    date = forms.DateField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
