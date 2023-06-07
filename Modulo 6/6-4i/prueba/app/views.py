from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def index(request):


    users = User.objects.all()
    context = {"usuarios": users}

    return render(request, "app/index.html", {'users': users}) #se agrega render para indicar que debe renderizar el template indicado

