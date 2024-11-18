## [Inicio](../index.md)
# Proyecto Primer Trimestre

En este proyecto se deseaba crear un programa que gestione una lista de tareas, cada tarea tiene asociado 4 datos:
1. Nombre de la tarea
2. Nivel de prioridad
3. Fecha de vencimiento
4. Si esta o no completada

En mi caso he decidido guardar las tareas en un diccionario en el que la clave es el nombre de la tarea y el valor es una lista con los 3 datos almacenados

Este programa tiene principalmente 6 funciones:
1. Añadir una nueva tarea
2. Listar todas las tareas
3. Marcar una tarea como completada
4. Eliminar una tarea
5. Guardar o cargar tareas desde un fichero
6. Listar las tareas que estan vencidas

Para ello he realizado una funcion para cada una (para cargar o guardar hay 3 ya que hay una para seleccionar si cargar o guardar y las otras son para cargar o guardar). A mayores hay una opcion mas en el menu que sirve para finalizar la ejecución.

Una vez realizado el programa, he realizado pruebas errores en cada uno de los metodos probando a introducir erroneamente los datos, a intentar eliminar tareas inexistente, listar las tareas cuando esta esta vacia... etc

## Codigo

```
from datetime import date, datetime
tareas = {
    "Tarea1" : [7, date(2024, 11, 18), False]
}

def agregarTarea():
    try:
        #Recogemos los datos necesarios
        nom = str(input("Introduce el nombre de la tarea: "))
        pri = int(input("Introduce el nivel de prioridad (1 - 10): "))
        fecha = str(input("Introduce la fecha de vencimiento (YYYY-MM-DD): "))
        completada = str(input("La tarea esta completada (Y/N): "))
        completada = completada.upper()
        fechaD = datetime.strptime(fecha, "%Y-%m-%d").date()
        #Comprobamos si esta realizada o no y la añadimos a la lista
        if(completada == "Y"):
            tareas[nom] = [pri, fechaD, True]
        else :
            tareas[nom] = [pri, fechaD, False]
    except Exception:
        print('\033[31m' + "\nDatos introducidos erroneos" + '\033[0m')
        print('\033[31m' + "Operacion cancelada \n" + '\033[0m')

def listarTareas():
    if(len(tareas) > 0):
        imprimir = "\nLista de Tareas: \n"
        contador = 1
        #Recorremos los nombres de las claves
        for a in tareas:
            imprimir += str(contador) + ". " + a + " | "
            lista = tareas[a]

            #Imprimimos los valores de la clave iterandolos
            for b in lista:

                #Comprobamos si es un boolean, si es asi es el final de cada tarea
                if (b == False or b == True):
                    if (b == True):
                        imprimir += "Completada \n"
                    else : 
                        imprimir += "No Completada \n"
                else :
                    imprimir += str(b) + " | "
            contador += 1

        #Imprimimos el resultado
        print(imprimir)
    else:
        print('\033[31m' + "\nNo hay tareas\n" + '\033[0m')

def completarTarea():
    try:
        #Recogemos el indice para identificar la tarea
        indiceDeseado = int(input("Introduce el indice de la tarea a completar: "))
        indice = 0
        resultado = False
        if(len(tareas) > (indiceDeseado - 1)):
            for a in tareas:

                #Comprobamos si es el indice deseado
                if (indice == (indiceDeseado - 1)):
                    lista = tareas[a]
                    if (lista[2] == False):
                        
                        #Cambiamos la tarea a True y mostramos un mensaje
                        tareas[a] = [lista[0], lista[1], True]
                        print('\033[32m' + "\nLa tarea " + a + " se ha completado \n" + '\033[0m')
                        resultado = True

                    else :
                        #Si la tarea indicada ya esta completada mostramos un mensaje
                        print('\033[31m' + "\nLa tarea indicada ya esta completada anteriormente \n" + '\033[0m')
                        resultado = True
                indice += 1
    except Exception:
        print('\033[31m' + "\nIndice introducido erroneo\n" + '\033[0m')

    #Si no se encontro la tarea mostramos un mensaje de error
    if(resultado == False):
        print('\033[31m' + "\nLa tarea indicada no existe\n" + '\033[0m')

def eliminarTarea():
    try:
        resultado = False
        #Recogemos el indice de la tarea a eliminar
        indiceDeseado = int(input("Introduce el indice de la tarea a eliminar: "))
        #Recorremos las tareas hasta llegar al indice seleccionado
        if(len(tareas) > (indiceDeseado - 1)):
            indice = 0
            for a in tareas:
                if (indice == (indiceDeseado - 1)):
                    #Guardamos el nombre de la tarea
                    nombreTarea = a
                indice += 1
            if(tareas.pop(nombreTarea) != None):
                    #Eliminamos la tarea
                    resultado = True
        #Comprobamos si se elimino correctamente y mostramos mensaje
        if(resultado):
            print('\033[32m' + "\nTarea eliminada con exito\n" + '\033[0m')
        else:
            print('\033[31m' + "\nLa tarea indicada no existe\n" + '\033[0m')
    except Exception:
        print('\033[31m' + "\nLa lista esta vacia\n" + '\033[0m')

def guardarEnFichero():
    #Abrimos el flujo hacia el fichero
    fichero = open("datos.csv", "w")
    cadenaEscribir = ""
    for a in tareas:
        #Recorremos cada tarea y ponemos los datos en una cadena separada de comas ','
        cadenaEscribir = a + ","
        lista = tareas[a]
        pri = lista[0]
        fecha = fecha_str = lista[1].strftime("%Y-%m-%d")
        completada = lista[2]
        cadenaEscribir += str(pri) + "," + fecha + "," + str(completada)
        cadenaEscribir += "\n"
        #Escribimos la linea en el fichero
        fichero.write(cadenaEscribir)
        print("Linea escrita: " + cadenaEscribir)
    fichero.close()

def cargardesdeFichero():
    try:
        #Abrimos el flujo hacia el fichero
        fichero = open("datos.csv", "r")
        #Leemos todas las lineas y las guardamos en una variable
        lineas = fichero.readlines()
        for linea in lineas:
            #Formateamos cada linea y eliminamos saltos de linea, espacios y separamos cada palabra
            lineaSinSalto = linea.strip()
            lista = lineaSinSalto.split(",")
            nombre = lista[0]
            prioridad = int(lista[1])
            fecha = datetime.strptime(lista[2], "%Y-%m-%d").date()
            completada = lista[3] == "True"
            #Creamos o sobreescribimos las tareas
            tareas[nombre] = [prioridad, fecha, completada]
            print("Linea cargada:" + lineaSinSalto)
            fichero.close()
    except FileNotFoundError:
        print('\033[31m' + "\nEl fichero no existe\n" + '\033[0m')
        fichero.close()
    except IOError:
        print('\033[31m' + "\nError en la lectura del fichero\n" + '\033[0m')
        fichero.close()

def cargarYGuardar():
    print("####### Operaciones #######")
    print("1. Guardar")
    print("2. Cargar")
    try:
        opcion = int(input("Elige una opcion: "))
        match(opcion):
            case 1:
                guardarEnFichero()
            case 2:
                cargardesdeFichero()
    except Exception:
        print('\033[31m' + "\nError al seleccionar la opcion \n" + '\033[0m')

def listarTareasVencidas():
    imprimir = "\nTareas Vencidas: \n"
    contador = 1
    resultado = False
    #Recorremos los nombres de las claves
    for a in tareas:
        lista = tareas[a]
        fecha = lista[1]
        fechaActual = date.today()
        #Comprobamos si la fecha es anterior a la actual
        if(fecha < fechaActual):
            resultado = True
            imprimir += str(contador) + ". " + a + " | "
            lista = tareas[a]
            for b in lista:
                if (b == False or b == True):
                    if (b == True):
                        imprimir += "Completada \n"
                    else : 
                        imprimir += "No Completada \n"
                else :
                    imprimir += str(b) + " | "
        contador += 1
    if(resultado):
        print(imprimir)
    else:
        print('\033[31m' + "\nNo hay tareas vencidas \n" + '\033[0m')

finalizado = True
while(finalizado):
    print("######### Menu #########")
    print("1. Añadir tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Guardar o cargar desde fichero")
    print("6. Listar Tareas Vencidas")
    print("7. Finalizar")
    try:
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
                listarTareasVencidas()
            case 7:
                finalizado = False
    except Exception:
        print('\033[31m' + "\nError al seleccionar la opcion\n" + '\033[0m')
```