from django import forms
from .models import Alumno, Curso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'matricula', 'departamento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'  # o especifica los campos: ['nombre', 'descripcion', 'fecha_inicio', ...]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'cupo_disponible': forms.NumberInput(attrs={'class': 'form-control'}),
            'docente': forms.TextInput(attrs={'class': 'form-control'}),
        }