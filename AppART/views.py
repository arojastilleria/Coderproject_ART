from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Docente, Administrador
from .forms import AlumnoForm, DocenteForm, AdministradorForm

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})

def detalle_alumno(request, id_alumno):
    alumno = get_object_or_404(Alumno, pk=id_alumno)
    return render(request, 'detalle_alumno.html', {'alumno': alumno})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tu_app:lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

# Vistas para Docentes y Administradores (análogas a las de Alumnos)

def lista_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'lista_docentes.html', {'docentes': docentes})

def detalle_docente(request, id_docente):
    docente = get_object_or_404(Docente, pk=id_docente)
    return render(request, 'detalle_docente.html', {'docente': docente})

def agregar_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tu_app:lista_docentes')
    else:
        form = DocenteForm()
    return render(request, 'agregar_docente.html', {'form': form})

def lista_administradores(request):
    administradores = Administrador.objects.all()
    return render(request, 'lista_administradores.html', {'administradores': administradores})

def detalle_administrador(request, id_administrador):
    administrador = get_object_or_404(Administrador, pk=id_administrador)
    return render(request, 'detalle_administrador.html', {'administrador': administrador})

def agregar_administrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tu_app:lista_administradores')
    else:
        form = AdministradorForm()
    return render(request, 'agregar_administrador.html', {'form': form})