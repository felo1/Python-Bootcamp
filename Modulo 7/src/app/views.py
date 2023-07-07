from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist
from .models import Tarea, TareaForm
from django.views.generic import ListView, UpdateView, DeleteView

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        tareas = Tarea.objects.filter(usuario=request.user).order_by('fecha_expiracion')
        return render(request, 'app/bienvenida.html', {'tareas': tareas})
    else:
        return render(request, 'app/index.html')

# original del gran rodri
#def detalles_tarea(request, id):
#    tareas = Tarea.objects.filter(usuario=request.user).order_by('fecha_expiracion')
#    tarea = Tarea.objects.get(id=request.GET['id'])
#    return render(request, 'app/tarea.html', {'tareas': tareas}, {'tarea': tarea})

#cambiado para tarea indi 3
def detalles_tarea(request, id):
    tareas = Tarea.objects.filter(usuario=request.user).order_by('fecha_expiracion')
    tarea = Tarea.objects.get(id=id)

    if request.method == 'POST':
        estado = request.POST.get('estado')
        if estado == 'completada':
            tarea.estado = 'Completada'
        elif estado == 'vista':
            tarea.estado = 'Vista'
        tarea.save()
        messages.success(request, 'Tarea editada exitosamente.')
        return HttpResponseRedirect(reverse('tareas-edit', args=[tarea.id]))

    return render(request, 'app/tarea.html', {'tareas': tareas, 'tarea': tarea})


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
            tareas = Tarea.objects.filter(usuario=request.user).order_by('fecha_expiracion')
            return render(request, 'app/bienvenida.html', {'tareas': tareas})
            #return HttpResponseRedirect(reverse("bienvenida"), {'tareas': tareas})
        else:
            context = ["Credenciales Inválidas"]#si no lo hago como lista, itera por cada caracter del string.
            return render(request, "app/login.html", {"messages": context})

    return render(request, "app/login.html") #view del login, en caso de fallo en login

@login_required
def bienvenida(request):

    tareas = Tarea.objects.exclude(estado="COMPLETADA").filter(usuario__username=request.user) #excluye completadas y luego filtra solo usuario logueado
 
    #ordering = ['-fecha_expiracion'] # el signo - es para ordenar de manor a mayor
    #return render(request, 'app/lista_tareas.html')

    context = {
        'username': request.user.username,
        'tareas': tareas
    }
    return render(request, "app/bienvenida.html", context)

@login_required
def logout_view(request):
    
    logout(request)
    return render(request, "app/logout.html")

@login_required
def crear_tarea(request):
    if request.method == 'POST': #si el usuario hace click en 'ingresar', el método pasa a ser POST
        
        form = TareaForm(request.POST) # se le pasa la información 'POST' al formulario
        if form.is_valid(): #si es válido, 
            tarea = form.save(commit=False) # guardar sin commit, porque falta el campo 'user.id' (no se ve en el formulario)
            tarea.usuario = User.objects.get(pk=request.user.id) # agregar campo del usuario logueado en ese momento
            tarea.save() # guardar ahora con commit
                
            messages.success(request, 'Tarea creada con èssito')
            return redirect('bienvenida') #redirige
    else:
        form = TareaForm() #al ingresar al view, se instancia un formulario vacío
        
    return render(request, "app/crear_tarea.html", {'form': form}) #render con contexto


class TareasListView(ListView): #listview es un class-based-view de django, que da la funcionalidad para mostrar datos en formato de lista.
    #los parámetros se asignan a variables
    model = Tarea #se indica modelo
    template_name = "app/bienvenida.html" #nombre del template
    ordering = ['fecha_expiracion'] #orden, se dan dos keys, porque la fecha y hora en mi modelo son dos variables separadas

    def get_context_data(self, **kwargs): #override del método de la clase padre, que es un generador de contexto para pasarlo al template
        context = super().get_context_data(**kwargs) #llama al método de la clase padre ListView usando super()
        tarea_form = TareaForm() #se instancia un formulario TareaForm vacío
        context['tarea_form'] = tarea_form #se agrega el tarea_form al dict de contexto 
        
        return context #contexto final

    def get_queryset(self): #override del método de la clase padre para obtener los queryset que necesitemos para dar la funcionalidad de filtrado
        queryset = super().get_queryset() #super() a la clase padre, para obtener el queryset inicial
        prioridad_filter = self.request.GET.get('prioridad_filter')
        estado_filter = self.request.GET.get('estado_filter') #si se ha seleccionado un filtro de estado, se asigna a esta variable
        #categoria_filter = self.request.GET.get('categoria_filter') #si se ha seleccionado un filtro de categoría, se asigna a esta variable
        #estas variables no se asignan si el usuario no selecciona filtros
        tarea_id = self.request.GET.get('tarea_id')
        user = self.request.user #se asigna el usuario logueado a una variable para usarlo más abajo.

        #si se cumplen las siguientes pruebas lógicas, se realiza un queryset con los parámetros indicados por los choicefields:

        if estado_filter and prioridad_filter: # si el usuario ha filtrado por estado Y categoría            
            queryset = queryset.filter(estado=estado_filter, prioridad=prioridad_filter,usuario=user)
        elif estado_filter:  # si el usuario ha filtrado sólo por estado,
            # Filtering by estado only
            queryset = queryset.filter(estado=estado_filter, usuario=user)
        elif prioridad_filter:
            queryset = queryset.filter(estado=estado_filter, usuario=user)
        else: #si el usuario no ha seleccionado filtros:
            queryset = queryset.filter(usuario=user)
        return queryset

    def post(self, request, *args, **kwargs): #override de post de la clase padre (ListView)
        tarea_id = request.POST.get('tarea_id') #obtiene el tarea_ide de los parámetros del POST, cada vez que se presiona "Completar" o "Eliminar"
        print(f"tarea_id = {tarea_id}")
        tarea = Tarea.objects.get(id=tarea_id) #obtiene el objeto Tarea asociado al tarea_id obtenido en la línea anterior.
        print(f"tarea = {tarea}")       

        if 'estado' in request.POST: #si en el POST viene un campo 'estado':
            tarea.estado = request.POST['estado'] #actualiza el campo con el valor correspondiente
        elif 'prioridad' in request.POST: #si en el POST viene un campo 'categoría':
            tarea.prioridad = request.POST['prioridad'] #acrualiza el campo con el valor correspondiente
        elif 'observaciones' in request.POST:
            tarea.observaciones = request.POST['observaciones']
        else:
            tarea.save()    
        tarea.save() #guarda
        return redirect('bienvenida') #redirige al listview, reflejándose el cambio de inmediato.

class TareaEditView(UpdateView): #Updateview es un class-based view usado para actualizar datos
    model = Tarea #se elige el modelo
    form_class = TareaForm #se elige el formulario
    template_name = "app/edit_tarea.html" #se elige el template

    def get_success_url(self): #override del metodo que la clase usa al completar exitosamente la edición. En este paso redirige al list-view
        return reverse('bienvenida')

    def get_object(self, queryset=None): #override del método de la clase padre.
        tarea = super().get_object(queryset) #obtiene el objeto tarea y lo asigna a esta variable
       
        tarea.save() #se guarda
        return tarea

class TareaDeleteView(DeleteView): #para borrar una tarea
    model = Tarea #se elige modelo

    def get_success_url(self): #cuando todo sale bien
        return reverse_lazy("bienvenida") #cundo se elimina una tarea con éxito, devuelve al listview

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tarea"] = self.object.id
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, "Tarea eliminada con éxito")
        return HttpResponseRedirect(bienvenida)