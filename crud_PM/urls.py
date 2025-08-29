"""
URL configuration for crud_PM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cursos import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    #cursos
    path('cursos/', views.consultar_cursos, name='consultar_cursos'),
    path('agregar/', views.agregar_curso, name='agregar_curso'),
    path('eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('cursos/editar/<int:id>/', views.editar_curso, name='editar_curso'),
    #alumnos
    path('alumnos/', views.listar_alumnos, name='listar_alumnos'),
    path('alumnos/agregar/', views.agregar_alumno, name='agregar_alumno'),
    path('alumnos/editar/<int:id>/', views.editar_alumno, name='editar_alumno'),
    path('alumnos/eliminar/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
    #docentes
    path('docentes/', views.lista_docentes, name='lista_docentes'),
    path('docentes/agregar/', views.crear_docente, name='crear_docente'),
    path('docentes/editar/<int:id_docente>/', views.editar_docente, name='editar_docente'),
    path('docentes/eliminar/<int:id_docente>/', views.eliminar_docente, name='eliminar_docente'),
]
