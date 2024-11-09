## [Unidad 4](../index.md)
# Practica 4
### Ejercicio1
```
frutas = {
    "Manzana" : 2,
    "Pera" : 3,
    "Platano" : 4,
    "Uva" : 4, 
    "Ciruela" : 2,
    "Higo" : 7,
    "Cereza" : 5,
}
respuesta = str(input("Introduce el nombre de una fruta: "))
resultado = False
for a in frutas:
    if(a == respuesta):
        resultado = True
if(resultado):
    print("El precio de " + respuesta + " es de: " + str(frutas.get(respuesta)) + "€")
else:
    print("La fruta introducida no existe")
```

### Ejercicio2
```
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

def resultadosSumas(diccionario):
    longitudLista = len(diccionario)
    contador = 0
    print("total categorias: " + str(longitudLista))
    resultado = 0
    for a in diccionario:
        resultado += sumaFilas(diccionario[a])
        print("Total de " + str(a) + ": " + str(sumaFilas(diccionario[a])))    
        contador += 1
    print("Total de productos: " + str(resultado))
        

def sumaFilas(lista):
    resul = 0
    for a in lista:
        resul += 1
    return resul

resultadosSumas(productos)
```

### Ejercicio3
```
frase = str(input("Introduce una frase: "))

fraseSeparada = frase.split(" ")
diccionario = {}
for a in fraseSeparada:
        diccionario[a] = (diccionario[a] + 1) if diccionario.get(a) != None else 1
print(diccionario)
```

### Ejercicio4
```
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
```

### Ejercicio5
```
def invertirDiccionario(diccionario):
    claves = []
    valores = []
    for a in diccionario:
        claves.append(a)
        valores.append(diccionario[a])
    nuevoDiccionario = {}
    indice = 0
    while (indice < len(claves)):
        nuevoDiccionario[valores[indice]] = claves[indice]
        indice += 1
    return nuevoDiccionario

dicc = {
    "gato":"animal",
    "pelota":"juguete",
    "arbol":"planta"
}

diccInver = invertirDiccionario(dicc)
print(diccInver)
```

### Ejercicio6
```
diccionario1 = {
    "Pelota":7.53,
    "Camiseta":10.00,
    "Llavero":5.00,
    "Deportivas": 39.99
}
diccionario2 = {
    "Camiseta":9.90,
    "Gafas de Sol":13.00,
    "Llavero":7.20,
    "Planta":23.67
}

nuevoDicc = {}

for a in diccionario1:
    if(diccionario2.get(a, "no") != "no"):
        valor = diccionario1[a] + diccionario2[a]
        nuevoDicc[a] = valor
    else :
        nuevoDicc[a] = diccionario1[a]
for b in diccionario2:
    if(nuevoDicc.get(b, "no") == "no"):
        nuevoDicc[b] = diccionario2[b]
print(nuevoDicc)
```

### Ejercicio7
```
umbral = float(input("introduce el umbral de salario: "))
diccionario = {
    "Paco":1200.00,
    "Maria":1300.00,
    "Luis":1500.00,
    "Jose":900.00
}
for a in diccionario:
    if(diccionario[a] > umbral):
        print(str(a) + ": " + str(diccionario[a]))
```

### Ejercicio8
```
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
```

### Ejercicio9
```
estudiantes = {
    "Ana": {"Matemáticas": 8.5, "Física": 9.0, "Programación": 7.8},
    "Carlos": {"Matemáticas": 9.2, "Física": 8.8, "Programación": 9.4},
    "Luis": {"Matemáticas": 7.6, "Física": 8.0, "Programación": 8.5},
    "María": {"Matemáticas": 9.5, "Física": 10.0, "Programación": 9.8},
    "Jorge": {"Matemáticas": 8.8, "Física": 8.4, "Programación": 7.9},
    "Sofía": {"Matemáticas": 9.1, "Física": 8.9, "Programación": 9.3}
}
diccionarioMediaEstudiante = {}
diccionarioMediaAsignatura = {}
for a in estudiantes:
    dicc = estudiantes[a]
    resultado = 0
    for b in dicc:
        resultado += dicc[b]
    resultado = resultado / len(dicc)
    diccionarioMediaEstudiante[a] = resultado
mates = 0
fisica = 0
progr = 0
for a in estudiantes:
    dicc = estudiantes[a]
    mates += dicc["Matemáticas"]
    fisica += dicc["Física"]
    progr += dicc["Programación"]
mates = mates / len(estudiantes)
fisica = fisica / len(estudiantes)
progr = progr / len(estudiantes)
diccionarioMediaAsignatura["Matemáticas"] = mates
diccionarioMediaAsignatura["Física"] = fisica
diccionarioMediaAsignatura["Programación"] = progr

print(diccionarioMediaEstudiante)
print(diccionarioMediaAsignatura)

```