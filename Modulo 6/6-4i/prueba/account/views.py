from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages #neceasrio para los mensajes de exito
#
#  Create your views here.

#def miembros(request):
#    username = request.POST["username"]
#    password = request.POST["password"]
#    user = authenticate(request, username=username, password=password)
#    if user is not None:
#        login(request, user)
#        # Redirect to a success page.
#        ...
#    else:
#        # Return an 'invalid login' error message.
#         ...

def miembros(request):
        return render(request, 'login_miembros.html')