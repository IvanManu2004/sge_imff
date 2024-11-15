tareas = {
    "Tarea1" : [7, "2005-01-01", False]
}

def agregarTarea():
    nom = str(input("Introduce el nombre de la tarea: "))
    pri = int(input("Introduce el nivel de prioridad (1 - 10): "))
    fecha = str(input("Introduce la fecha de vencimiento (YYYY-MM-DD): "))
    completada = str(input("La tarea esta completada (Y/N): "))
    if(completada == "Y"):
        tareas[nom] = [pri, fecha, True]
    else :
        tareas[nom] = [pri, fecha, False]

def listarTareas():
    for a in tareas:
        imprimir = a + " | "
        lista = tareas[a]
        for b in lista:
            if (b == False or b == True):
                if (b == True):
                    imprimir += "Completada"
                else : 
                    imprimir += "No Completada"
            else :
                imprimir += str(b) + " | "
        print(imprimir)

def completarTarea():
    indiceDeseado = int(input("Introduce el indice de la tarea a completar: "))
    indice = 0
    if(len(tareas) > (indiceDeseado - 1)):
        for a in tareas:
            if (indice == (indiceDeseado - 1)):
                lista = tareas[a]
                if (lista[2] == False):
                    tareas[a] = [lista[0], lista[1], True]
                    print("La tarea " + a + " se ha completado")
                else :
                    print("La tarea indicada ya esta completada anteriormente")
            indice += 1

def eliminarTarea():
    resultado = False
    indiceDeseado = int(input("Introduce el indice de la tarea a eliminar: "))
    if(len(tareas) > (indiceDeseado - 1)):
        indice = 0
        for a in tareas:
            if (indice == (indiceDeseado - 1)):
                nombreTarea = a
            indice += 1
        if(tareas.pop(nombreTarea) != None):
                resultado = True
    if(resultado):
        print("Tarea eliminada con exito")
    else:
        print("La tarea indicada no existe")

def guardarEnFichero():
    fichero = open("datos.csv", "w")
    cadenaEscribir = ""
    for a in tareas:
        cadenaEscribir = a + ","
        lista = tareas[a]
        for b in lista:
            cadenaEscribir += str(b) + ","
        cadenaEscribir += "\n"
        fichero.write(cadenaEscribir)
        print("Linea escrita: " + cadenaEscribir)
    fichero.close()

def cargardesdeFichero():
    try:
        fichero = open("datos.csv", "r")
        lineas = fichero.readlines()
        for linea in lineas:
            lineaSinSalto = linea.strip()
            lista = lineaSinSalto.split(",")
            if(lista[3] == "True"):
                completada = True
            else :
                completada = False
            tareas[lista[0]] = [int(lista[1]), lista[2], completada]
            print("Linea cargada:" + lineaSinSalto)
            fichero.close()
    except FileNotFoundError:
        print("El fichero no existe")
        fichero.close()
    except IOError:
        print("Error en la lectura del fichero")
        fichero.close()

def cargarYGuardar():
    print("####### Operaciones #######")
    print("1. Guardar")
    print("2. Cargar")
    opcion = int(input("Elige una opcion: "))
    match(opcion):
        case 1:
            guardarEnFichero()
        case 2:
            cargardesdeFichero()

finalizado = True
while(finalizado):
    print("######### Menu #########")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Guardar o cargar desde fichero")
    print("6. Finalizar")
    opcion = int(input("Elige una opcion: "))
    match(opcion):
        case 1:
            agregarTarea()
        case 2:
            listarTareas()
        case 3:
            completarTarea()
        case 4:
            eliminarTarea()
        case 5:
            cargarYGuardar()
        case 6:
            finalizado = False