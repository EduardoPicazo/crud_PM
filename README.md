# CRUD Cursos-Hospital

📖 Resumen:
Este proyecto es un CRUD desarrollado en Django para administrar cursos medicos que son impartidos en un hospital
para la formacion del personal que labora en la institución.
Permite la gestión de docentes, alumnos y cursos, incluyendo la visualizacion, la creacion, modificacion y eliminación
de los registros.

Para el almacenamiento de datos, el sistema se conecta con una base de datos MariaDB.


🗄️ Modelo Entidad-Relación (ER):
El modelo de datos define la relación entre los docentes, cursos y alumnos.

* Un docente puede impartir varios cursos.
* Un curso puede tener varios alumnos.
* Un alumno puede estar inscrito en varios cursos.