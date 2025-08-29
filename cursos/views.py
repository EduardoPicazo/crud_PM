from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Curso, Alumno, Docente
from .forms import LoginForm, AlumnoForm, DocenteForm
from cursos.models import Curso, CursoForm

# Create your views here.
#Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home') #nos redirigimos a la pagina principal
        else:
            messages.error(request, 'Por favor, ingresa un usuario y contraseña válidos.')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

@login_required(login_url='login')
def home_view(request):
    return render(request, 'inicio.html')

def logout_view(request):
    logout(request)
    return redirect('login')

#Cursos
def consultar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def agregar_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultar_cursos') 
    else:
        form = CursoForm()

    return render(request, 'agregar_curso.html', {'form': form})


def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    curso.delete()
    messages.success(request, "Curso eliminado con éxito.")
    return redirect('consultar_cursos') 

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":
        curso.nombre = request.POST.get("nombre")
        curso.descripcion = request.POST.get("descripcion")
        curso.fecha_inicio = request.POST.get("fecha_inicio")
        curso.fecha_cierre = request.POST.get("fecha_cierre")
        curso.horario = request.POST.get("horario")
        curso.cupo_disponible = request.POST.get("cupo_disponible")
        curso.docente = request.POST.get("docente")

        curso.save()
        messages.success(request, "El curso ha sido actualizado correctamente.")

    return redirect("consultar_cursos")

#Alumnos 

def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'agregar_alumno.html', {'form': form})

def editar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'editar_alumno.html', {'form': form, 'alumno': alumno})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        alumno.delete()
        return redirect('listar_alumnos')
    return render(request, 'eliminar_alumno.html', {'alumno': alumno})

#Docentes
def lista_docentes(request):
    docentes = Docente.objects.all()
    form = DocenteForm()
    return render(request, 'docentes.html', {'docentes': docentes, 'form': form})

def crear_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Docente registrado correctamente ✅")
            return redirect('lista_docentes')
        else:
            messages.error(request, "Corrige los errores del formulario ❌")
            return redirect('lista_docentes')


def editar_docente(request, id_docente):
    docente = get_object_or_404(Docente, pk=id_docente)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
    return redirect('lista_docentes')

def eliminar_docente(request, id_docente):
    try:
        docente = get_object_or_404(Docente, pk=id_docente)
        docente.delete()
        messages.success(request, f"El docente '{docente.nombre}' fue eliminado correctamente ✅")
    except Exception as e:
        messages.error(request, f"No se pudo eliminar el docente ❌: {e}")
    return redirect('lista_docentes')