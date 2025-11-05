# -*- coding: utf-8 -*-
''' Realizar lo siguiente:
    1. Comentar los atributos de cada una de las clases.
    2. Agregar atributos a cada una de las clases (con base en sus diagramas de clase). Estos
    atributos tienen que recibir las mismas acciones que los demás.
    3. Guardar los datos en un archivo .txt '''

class Alumno:
    #Agregar
    def __init__(self, nombre: str, numero_control: str, carrera=None):
        self.nombre = nombre
        self.numero_control = numero_control
        self.carrera = carrera                
        self.calificaciones = {}              

    def asignar_carrera(self, carrera):
        self.carrera = carrera

    def consulta_calificacion(self, nombre_materia: str):
        if nombre_materia in self.calificaciones:
            return self.calificaciones[nombre_materia]
        else:
            return f'No hay calificación registrada para "{nombre_materia}".'

    def __repr__(self):
        return f'Alumno("{self.nombre}", "{self.numero_control}")'


class Universidad:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.carreras = []      
        self.alumnos = []       
        self.profesores = []     

    # ------------------- Gestión de carreras -------------------
    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carrera(self, nombre_carrera: str):
        for c in self.carreras:
            if c.nombre == nombre_carrera:
                return c
        return None

    # ------------------- Otros registros -------------------
    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def agregar_profesor(self, profesor):
        self.profesores.append(profesor)


class Carrera:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.materias = []   # Lista de objetos Materia

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def obtener_materia(self, nombre_materia: str):
        for m in self.materias:
            if m.nombre == nombre_materia:
                return m
        return None

    def __repr__(self):
        return f'Carrera("{self.nombre}")'


class Materia:
    def __init__(self, nombre: str, carrera: Carrera, calificacion_final: float = None):
        self.nombre = nombre
        self.carrera = carrera                 
        self.calificacion_final = calificacion_final

    def __repr__(self):
        return f'Materia("{self.nombre}", carrera="{self.carrera.nombre}")'


class Profesor:
    def __init__(self, nombre: str, materia: Materia):
        self.nombre = nombre
        self.materia = materia                 

    def registra_calificacion(self, alumno: Alumno, calificacion: float):
        alumno.calificaciones[self.materia.nombre] = calificacion
        print(f'Calificación registrada: {alumno.nombre} -> '
              f'{self.materia.nombre}: {calificacion}')

    def __repr__(self):
        return f'Profesor("{self.nombre}", {self.materia})'

if __name__ == "__main__":

    uni = Universidad("Instituto")

    ing = Carrera("Ingeniería")
    lic = Carrera("Licenciatura en Ciencias Sociales")

    uni.agregar_carrera(ing)
    uni.agregar_carrera(lic)

    calc = Materia("Cálculo I", ing)
    fis = Materia("Física I", ing)
    sociologia = Materia("Introducción a la Sociología", lic)

    ing.agregar_materia(calc)
    ing.agregar_materia(fis)
    lic.agregar_materia(sociologia)

    juan = Alumno("Juan Pérez", "2023001")
    luisa = Alumno("Luisa Gómez", "2023002")

    juan.asignar_carrera(ing)
    luisa.asignar_carrera(ing)

    uni.agregar_alumno(juan)
    uni.agregar_alumno(luisa)

    prof_garcia = Profesor("Dr. García", calc)
    prof_rodriguez = Profesor("Mtra. Rodríguez", fis)

    uni.agregar_profesor(prof_garcia)
    uni.agregar_profesor(prof_rodriguez)

    prof_garcia.registra_calificacion(juan, 8.5)
    prof_garcia.registra_calificacion(luisa, 9.0)
    prof_rodriguez.registra_calificacion(juan, 7.5)

    print(juan.consulta_calificacion("Cálculo I"))   
    print(juan.consulta_calificacion("Física I"))   
    print(luisa.consulta_calificacion("Cálculo I")) 
    print(luisa.consulta_calificacion("Física I"))  

    print("Materias de Ingeniería:", [m.nombre for m in ing.materias])
