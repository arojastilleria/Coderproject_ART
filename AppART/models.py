from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    correo_electronico = models.EmailField()

    class Meta:
        abstract = True  # Marca esta clase como abstracta para que no se cree una tabla en la base de datos

# Clase que representa a un alumno
class Alumno(Persona):
    # Puedes agregar campos específicos para Alumno si es necesario
    numero_alumno = models.CharField(max_length=10)

# Clase que representa a un docente
class Docente(Persona):
    # Puedes agregar campos específicos para Docente si es necesario
    numero_empleado = models.CharField(max_length=10)

# Clase que representa a un administrador
class Administrador(Persona):
    # Puedes agregar campos específicos para Administrador si es necesario
    numero_administrador = models.CharField(max_length=10)
