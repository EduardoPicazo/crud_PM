from django.db import models
from django.core.validators import RegexValidator
from django import forms

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField()
    horario = models.CharField(max_length=100)
    cupo_disponible = models.IntegerField()
    docente = models.CharField(max_length=100)


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_cierre', 'horario', 'cupo_disponible', 'docente']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_cierre': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'cupo_disponible': forms.NumberInput(attrs={'class': 'form-control'}),
            'docente': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=120)  # Cambié a EmailField
    telefono = models.CharField(max_length=15, blank=True, null=True)
    matricula = models.CharField(max_length=20, unique=True)
    departamento = models.CharField(max_length=100)  # Corregí "departamneto" a "departamento"
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Mejor usar DateTimeField con auto_now_add
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=10, unique=True, blank=False,
                                validators=[RegexValidator(
                                    regex=r'^[A-Z0-9]+$', message="La matrícula solo puede contener mayúsculas y números"
                                )])
    nombre = models.CharField(max_length=50, blank=False, validators=[
        RegexValidator(
            regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', message="El nombre solo puede contener letras"
        )])
    apellidos = models.CharField(max_length=50, blank=False, validators=[
        RegexValidator(
            regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El apellido solo puede contener letras"
        )])
    especialidad = models.CharField(max_length=100, blank=False, validators=[
        RegexValidator(
            regex=r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$',
                message="El la especialidad solo puede contener letras"
        )])
    telefono = models.CharField(max_length=10, blank=False, validators=[
        RegexValidator(
            regex=r'^\+?[0-9]+$',
                message="El teléfono solo puede contener números y el signo +"
        )])
    correo = models.EmailField(unique=True, blank=False,)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"