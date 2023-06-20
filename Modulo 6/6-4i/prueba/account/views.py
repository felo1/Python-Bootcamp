from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages #neceasrio para los mensajes de exito
#
#  Create your views here.

def login_view(request):
  if 'next' in request.GET:
        #si en la url está la palabra "next", generada al redirigir desde @login_required, enviar mensaje.
        messages.add_message(request, messages.INFO, 'No no, esas funcionalidades son para usados logueados')

  if request.method == "POST":      
    username = request.POST["usuario"] #en comillas es el nombre del input en el formulario 
    #desde donde viene esta información. En este caso el nombre inputfield para el username es "usuario"
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    #en esta linea usamos funcionalidad integrada para contrastar los datos provistos con 
    #la base de datos 
    if user:
        login(request, user)
        messages.success(request, f'Usuario {username} logueado exitosamente!!')
        return redirect('welcome')
        #aca volver a una página de exito, por ahora el home
    else:
        context= ["Credenciales Inválidas"]
        return render(request, 'index.html', {"messages": context})
  
  return render(request, "login.html") #view del login

#def miembros(request):
#        return render(request, 'login_miembros.html')

@login_required(login_url="login")
def welcome_view(request):
        return render(request, 'welcome.html')

def logout_view(request):
      #user = authenticate.user
      logout(request)
      context= [f"Vuelve pronto!"]
      return render(request, "login.html")