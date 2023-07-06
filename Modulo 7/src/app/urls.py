"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    #path("bienvenida", views.bienvenida, name="bienvenida"),
    path("crear_tarea", views.crear_tarea, name="crear_tarea"),
    path("bienvenida", views.TareasListView.as_view(), name="bienvenida"),
    path("listview_tareas", views.TareasListView.as_view(), name="tareas-list"),
    #path('detalles_tarea/<int:tarea_id>/', views.detalles_tarea, name="detalles_tarea"),
    path('detalles_tarea/<id>/', views.detalles_tarea, name="detalles_tarea"),
    path('tareas/<int:pk>/edit/', views.TareaEditView.as_view(), name='tareas-edit'),
    path('tareas/<int:pk>/delete/', views.TareaDeleteView.as_view(), name='tareas-delete'),

]
