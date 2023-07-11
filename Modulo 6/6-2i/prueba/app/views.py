from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return(render(request, "app/index.html")) #se agrega render para indicar que debe renderizar el template indicado

