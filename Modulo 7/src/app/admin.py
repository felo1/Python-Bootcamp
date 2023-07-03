from django.contrib import admin
from .models import Producto, Cliente, Categoria, Tarea, ListaTarea
# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Tarea)
admin.site.register(Categoria)