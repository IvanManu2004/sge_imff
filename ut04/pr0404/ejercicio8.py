departamentos = {
    "Recursos Humanos": {
        "Ana": "Gerente de Recursos Humanos",
        "Luis": "Especialista en Reclutamiento",
        "Elena": "Asistente de Recursos Humanos"
    },
    "Tecnología": {
        "Carlos": "Desarrollador Backend",
        "María": "Desarrolladora Frontend",
        "Pedro": "Administrador de Sistemas"
    },
    "Marketing": {
        "Sofía": "Directora de Marketing",
        "Jorge": "Especialista en SEO",
        "Laura": "Community Manager"
    },
    "Finanzas": {
        "Juan": "Analista Financiero",
        "Lucía": "Contadora",
        "Raúl": "Asesor Financiero"
    }
}

salir = True
while (salir):
    print("1. Mostrar el listado de todos los empleados de un departamento")
    print("2. Añadir un empleado a un departamento")
    print("3. Eliminar un empleado de un departamento")
    print("4. Salir")
    opcion = int(input("Selecciona una opcion: "))
    match(opcion):
        case 1:
            dept = str(input("Introduce el nombre de un departamento: "))
            for a in departamentos[dept]:
                print(" - " + str(a) + " | " + str(departamentos[dept][a]))
        case 2:
            depar = str(input("Introduce el nombre de un departamento: "))
            nombre = str(input("Introduce el nombre del empleado: "))
            puesto = str(input("Introduce su puesto de trabajo: "))
            departamentos[depar][nombre] = puesto
        case 3: 
            depart = str(input("Introduce el nombre de un departamento: "))
            nombre = str(input("Introduce el nombre del empleado: "))
            departamentos[depart].pop(nombre)
        case 4:
            salir = False