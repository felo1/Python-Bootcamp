from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserRegistrationForm #requerido para este tipo de formularios built-in
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
from django.contrib import messages

def index(request):
 
   users = User.objects.all()
   context = {"usuarios": users}
   return render(request, "index.html", {'users': users})
#acá estoy al cargar mi index solicitando cargar en la variable users todos mis usuarios desde la BD
#para luegos pasarselos al contexto (en una variable llamada igualmente users) para ser renderizada.
#se agrega render para indicar que debe renderizar el template indicado
@permission_required('Administradores', login_url='index', raise_exception=True)
def forms(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('index') #requiere import de django shortcuts (redirect)
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'formulario.html', context=context)

@permission_required('Administradores', login_url='index', raise_exception=True) #esto nos permite tener
#un nivel adicional de restricciones.
#TODO: Que no te mande un 403 si no que te devuelva al index pero con un mensaje
def usuarios(request):
        users = User.objects.all()
        context = {"usuarios": users}
        return render(request, "usuarios.html", {'users': users})
    