asignaturas = {
    "Matematicas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Fisica": ["Elena", "Luis", "Juan", "Sofía"],
    "Programacion": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Ingles": ["Carlos", "Sofía", "Jorge", "María"],
}
salir = True
while (salir):
    print("1. Listar estudiantes matriculados en una asignatura")
    print("2. Matricular un estudiante en una asignatura")
    print("3. Dar de baja un estudiante de una asignatura")
    print("4. Salir")
    opcion = int(input("Selecciona una opcion: "))
    match(opcion):
        case 1:
            asig = str(input("Introduce el nombre de la asignatura: "))
            for a in asignaturas[asig]:
                print("- " + a)
        case 2:
            nombre = str(input("Introduce el nombre del alumno a matricular: "))
            asign = str(input("Introduce el nombre de la asignatura: "))
            asignaturas[asign].append(nombre)
        case 3: 
            nombreElim = str(input("Introduce el nombre del alumno a dar de baja: "))
            asigna = str(input("Introduce el nombre de la asignatura: "))
            asignaturas[asigna].pop(asignaturas[asigna].index(nombreElim))
        case 4:
            salir = False

