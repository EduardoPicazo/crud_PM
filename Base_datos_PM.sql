-- Crear base de datos
CREATE DATABASE hospital_cursos;
USE hospital_cursos;

-- ==========================
-- Tabla de DOCENTES
-- ==========================
CREATE TABLE docentes (
    id_docente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(120) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    especialidad VARCHAR(100),
    numero_empleado VARCHAR(50) UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================
-- Tabla de ALUMNOS
-- ==========================
CREATE TABLE alumnos (
    id_alumno INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(120) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    matricula VARCHAR(50) UNIQUE,
    departamento VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================
-- Tabla de CURSOS
-- ==========================
CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    horario VARCHAR(100),
    modalidad ENUM('presencial','online','mixto') DEFAULT 'presencial',
    cupos_disponibles INT DEFAULT 0,
    estado ENUM('disponible','no_disponible','finalizado') DEFAULT 'disponible',
    id_docente INT,
    FOREIGN KEY (id_docente) REFERENCES docentes(id_docente)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- ==========================
-- Tabla de INSCRIPCIONES
-- ==========================
CREATE TABLE inscripciones (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_alumno INT NOT NULL,
    id_curso INT NOT NULL,
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado ENUM('activo','finalizado','retirado') DEFAULT 'activo',
    calificacion DECIMAL(5,2),
    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (id_alumno, id_curso) -- Evita que un alumno se inscriba 2 veces al mismo curso
);
