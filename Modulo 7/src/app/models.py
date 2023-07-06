from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Tarea(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nombre de la actividad")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_expiracion = models.DateField(default=None, null=True, blank=True)
    PRIORIDAD_opciones = (
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('máxima', 'Máxima'),
    )
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_opciones)
    estado_opciones = (
        ('asignada', 'Asignada'),
        ('vista', 'Vista'),
        ('completada', 'Completada'),
        ('en reasignación', 'En reasignación'),
        ('anulada', 'Anulada'),
    )
    estado = models.CharField(max_length=15, choices=estado_opciones, verbose_name="Estado de la actividad")
    def __str__(self):
        return self.name + ' | Responsable: ' + str(self.usuario)
    
class ListaTarea(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Tarea)
    #la lista de tareas es una tabla intermedia que vincula tareas varias con un solo usuario.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio_base = models.IntegerField()
    sku = models.CharField(max_length=15)
    stock = models.IntegerField(default=0)
    #proveedor = models.ForeignKey('Proveedor', blank=True)  # 
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default=None)
    
class Cliente(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    rut = models.CharField(max_length=11)
    telefono_movil = models.CharField(max_length=30, default="", blank=True)
    telefono_fijo = models.CharField(max_length=30, default="", blank=True)
    email = models.CharField(max_length=30, default="", blank=True)
    notas = models.CharField(max_length=250, default="", blank=True)
    direcciones = models.CharField(max_length=250, default="", blank=True)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos
    
