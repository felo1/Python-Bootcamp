from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
import datetime
from django.contrib.auth.models import Group, User
# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def login_view(request): #el form está directo en el template login.html
    if 'next' in request.GET:
        #si en la url está la palabra "next", generada al redirigir desde @login_required, enviar mensaje.
        messages.add_message(request, messages.INFO, 'Debe ingresar para acceder a las funcionalidades.')

    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user:
            
            login(request, user)
          
            return HttpResponseRedirect(reverse("bienvenida"))
        else:
            context = ["Credenciales Inválidas"]#si no lo hago como lista, itera por cada caracter del string.
            return render(request, "app/login.html", {"messages": context})

    return render(request, "app/login.html") #view del login

def bienvenida(request):
    context = {
        'username': request.user.username,
        # add other context variables if needed
    }
    return render(request, "app/bienvenida.html", context)

def logout_view(request):
    
    logout(request)
    return render(request, "app/logout.html")
