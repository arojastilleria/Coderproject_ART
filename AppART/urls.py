from django.urls import path
from . import views

app_name = "AppART"

urlpatterns = [

    path('', views.inicio, name='inicio'),
        # Rutas para Alumnos
    path('alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('alumnos/<int:id_alumno>/', views.detalle_alumno, name='detalle_alumno'),
    path('alumnos/agregar/', views.agregar_alumno, name='agregar_alumno'),


    # Rutas para Docentes
    path('docentes/', views.lista_docentes, name='lista_docentes'),
    path('docentes/<int:id_docente>/', views.detalle_docente, name='detalle_docente'),
    path('docentes/agregar/', views.agregar_docente, name='agregar_docente'),


    # Rutas para Administradores
    path('administradores/', views.lista_administradores, name='lista_administradores'),
    path('administradores/<int:id_administrador>/', views.detalle_administrador, name='detalle_administrador'),
    path('administradores/agregar/', views.agregar_administrador, name='agregar_administrador'),
    
       
    
    
    
    
    
    ]