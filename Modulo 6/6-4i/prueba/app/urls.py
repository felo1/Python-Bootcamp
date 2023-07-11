from django.urls import path
from . import views # para que más abajo se pueda usar views.index

urlpatterns = [
    path('', views.index, name = "index"),
    path('forms', views.forms, name='forms'), 
    path('users', views.usuarios, name='users'), 
    #por simpleza, usar el mismo nombre en views."forms" con el método a usar en la vista, 
    #y en el nombre del archivo que irá en los templates
    #path('register_user/', views.register_user, name='register_user'),
    # "" es lo que sigue de la url principal, en este caso es solo /, 
    # el segundo parámetro es lo que se debe renderizar al ingresar allí.
    #el tercer parámetro es para poder referenciar desde otras partes de la app.
]