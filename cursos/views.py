from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from cursos.models import Curso, CursoForm

# Create your views here.
def login (request):
    return render(request, "inicio.html")



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