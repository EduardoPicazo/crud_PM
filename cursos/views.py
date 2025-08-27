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

