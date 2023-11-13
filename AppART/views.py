from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Docente, Administrador


#vista de inicio

def inicio(request):
    return render(request, "inicio.html")



def alumno (req):

    return render(req, "alumno.html")


def docente (req):

    return render(req, "docente.html")





def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'lista_alumnos.html', {'alumnos': alumnos})

def detalle_alumno(request, id_alumno):
    alumno = get_object_or_404(Alumno, pk=id_alumno)
    return render(request, 'detalle_alumno.html', {'alumno': alumno})

def agregar_alumno(request):
    if request.method == 'POST':
        # Aquí deberías procesar los datos del formulario si los tienes,
        # o simplemente realizar la acción deseada si no tienes un formulario.
        return redirect('AppART :lista_alumnos')
    else:
        # Aquí puedes mostrar un formulario si lo necesitas.
        return render(request, 'agregar_alumno.html', {})

# Vistas para Docentes y Administradores (análogas a las de Alumnos)

def lista_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'lista_docentes.html', {'docentes': docentes})

def detalle_docente(request, id_docente):
    docente = get_object_or_404(Docente, pk=id_docente)
    return render(request, 'detalle_docente.html', {'docente': docente})

def agregar_docente(request):
    if request.method == 'POST':
        # Procesar datos del formulario o realizar la acción deseada.
        return redirect('AppART:lista_docentes')
    else:
        # Mostrar un formulario si es necesario.
        return render(request, 'agregar_docente.html', {})

def lista_administradores(request):
    administradores = Administrador.objects.all()
    return render(request, 'lista_administradores.html', {'administradores': administradores})

def detalle_administrador(request, id_administrador):
    administrador = get_object_or_404(Administrador, pk=id_administrador)
    return render(request, 'detalle_administrador.html', {'administrador': administrador})

def agregar_administrador(request):
    if request.method == 'POST':
        # Procesar datos del formulario o realizar la acción deseada.
        return redirect('AppART:lista_administradores')
    else:
        # Mostrar un formulario si es necesario.
        return render(request, 'agregar_administrador.html', {})