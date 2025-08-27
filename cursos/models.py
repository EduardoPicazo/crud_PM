from django.db import models
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
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=120)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    matricula = models.CharField(max_length=20, unique=True)
    departamneto = models.CharField(max_length=100)
    fecha_registro = models.DateField()





