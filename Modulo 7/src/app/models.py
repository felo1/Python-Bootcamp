from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Tareas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

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
    
