## [Unidad 4](../index.md)
# Practica 2
### Ejercicio1
```
def cuantasLetras (cadena):
        i = 0
        cuentaVocales = 0
        vocales={"a", "e", "i", "o", "u"}
        for vocal in vocales:
           cuentaVocales += cadena.lower().count(vocal) 
        for a in cadena:
            i += 1
        cuentaConsonantes = i - cuentaVocales
        print("La cadena tiene " + str(cuentaVocales) + " vocales y " + str(cuentaConsonantes) + " consonantes")
palabras = str(input("Introduce una cadena: "))
cuantasLetras(palabras)
```

### Ejercicio2
```
palabra = str(input("Introduce una cadena: "))
print(palabra[::-1])
```

### Ejercicio3
```
palabra = str(input("Introduce una palabra: "))
if (palabra == palabra[::-1]):
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")
```

### Ejercicio4
```
def contarPalabras(cadenaContar):
    i = 0
    for a in cadena.split(" "):
        i += 1
    return i
cadena = str(input("Introduce una cadena separada por espacios: "))
numPalabras = contarPalabras(cadena)
print("Hay " + str(numPalabras) + " palabras")
```

### Ejercicio5
```
def eliminarRepeticiones (cadena):
    contadorCadena = 0
    for a in cadena:
        contadorCadena+=1
    cadenaLista = list(cadena)
    indice = 1
    indiceAnterior = 0
    while (indice < contadorCadena):
        letra1 = cadenaLista[indiceAnterior]
        letra2 = cadenaLista[indice]
        if (letra1 == letra2):
            cadenaLista.pop(indice)
            contadorCadena-=1
        else:
            indiceAnterior+=1
            indice+=1
    nuevaCadena = ""
    for a in cadenaLista:
       nuevaCadena += a
    print(str(nuevaCadena)) 
    
frase = str(input("Introduce una cadena: "))
eliminarRepeticiones(frase)
```

### Ejercicio6
```
cadena = str(input("Introduce una cadena: "))
contadorCadena = 0
for a in cadena:
    contadorCadena+=1
cadenaLista = list(cadena)
indice = 0
nuevaCadena = ""
while (indice < contadorCadena):
    letra = cadenaLista[indice]
    if (letra.isupper()):
        nuevaCadena += letra.lower()
    else :
        nuevaCadena += letra.upper()
    indice+=1

print(str(nuevaCadena)) 
```

### Ejercicio7
```
cadena = str(input("Introduce una cadena: "))
contadorCadena = 0
cadenasSeparadas = cadena.split(" ")
for a in cadenasSeparadas:
    contadorCadena+=1
indice = 0
nuevaCadena = ""
while (contadorCadena > indice):
    contadorCadena -= 1
    palabra = cadenasSeparadas[contadorCadena]
    nuevaCadena += palabra + " "

print(str(nuevaCadena)) 
```

### Ejercicio8
```
palabra1 = str(input("Introduce una palabra: "))
palabra2 = str(input("Introduce una palabra: "))
resultado = True
cadena1 = list(palabra1)
for a in cadena1:
    if(palabra2.count(a) == 0):
        resultado = False
if(resultado):
    print("Las dos palabras son anagramas") 
else:
    print("Las dos palabras no son anagramas") 
```

### Ejercicio9
```
def diccionarioCaracteres (cadena):
    listaLetras = list(cadena)
    indice = 0
    contadorLetras = 0
    for a in cadena:
        contadorLetras+=1
    diccionario = {}
    while (int(indice) < contadorLetras):
        diccionario["letra"+str(indice)] = listaLetras[indice]
        indice += 1
    print(diccionario)


frase = str(input("Introduce una cadena: "))
diccionarioCaracteres(frase)
```

### Ejercicio10
```
cadena = str(input("Introduce una cadena: "))
contadorCadena = 0
caracteres = list(cadena)
for a in caracteres:
    contadorCadena+=1
indice = 0
nuevaCadena = ""
while (indice < contadorCadena):
    letra = caracteres[indice]
    if(letra.isalnum() or letra==" "):
        nuevaCadena += letra
    indice += 1

print(str(nuevaCadena)) 
```

### Ejercicio11
```
cadena = str(input("Introduce una cadena: "))
cadenaSeparada = cadena.split(" ")
nuevaCadena = cadenaSeparada[0]
for palabra in cadenaSeparada[1:]:
    nuevaCadena += palabra.title()
print(nuevaCadena)
```

### Ejercicio12
```
def codificarRLE (cadena):
    cadenaSeparada = cadena.split(" ")
    nuevaCadena = ""
    for palabra in cadenaSeparada:
        letraAnterior = ""
        for letra in palabra:
            if letraAnterior == "":
                letraAnterior = letra
                contador = 1
            elif letraAnterior == letra:
                contador += 1
            else:
                nuevaCadena += letraAnterior + str(contador)
                letraAnterior = letra
                contador = 1
        nuevaCadena += letraAnterior + str(contador)
        letraAnterior = letra
        contador = 1
        nuevaCadena += " "
    print(nuevaCadena)

    
frase = str(input("Introduce una cadena: "))
codificarRLE(frase)
```

### Ejercicio13
```
def decodificarRLE (cadena):
    cadenaSeparada = cadena.split(" ")
    nuevaCadena = ""
    for palabra in cadenaSeparada:
        letraC = ""
        for letra in palabra:
            if letra.isalpha():
                letraC= letra
            elif letra.isdigit():
                nuevaCadena += letraC * int(letra)
        nuevaCadena += " "
    print(nuevaCadena)

    
frase = str(input("Introduce una cadena RLE: "))
decodificarRLE(frase)
```

### Ejercicio14
```
cadena = "Hola {nombre} felices {edad} años"
diccionario = {
    "nombre": "Ivan",
    "edad": 20,
}
cadenaSeparada = cadena.split(" ")
cadenaNueva = ""
for palabra in cadenaSeparada:
    if (palabra.count("{") == 1):
        palabraSinCorchetes = palabra[1:-1]
        cadenaNueva += str(diccionario[palabraSinCorchetes])
    else:
        cadenaNueva += palabra
    cadenaNueva += " "
print(cadenaNueva)
```

### Ejercicio15
```
def compararASCII(cadena1, cadena2):
    palabrasCadena1 = cadena1.split(" ")
    palabrasCadena2 = cadena2.split(" ")
    contadorCadena1 = 0
    contadorCadena2 = 0
    for palabra in palabrasCadena1:
        for letra in palabra:
            contadorCadena1 += ord(letra)
    for palabra in palabrasCadena2:
        for letra in palabra: 
            contadorCadena2 += ord(letra)
    if(contadorCadena1 > contadorCadena2):
        print("La cadena 1 es mayor en valor ASCII")
    else :
        print("La cadena 2 es mayor en valor ASCII")
    print("Cadena1: " + str(contadorCadena1))
    print("Cadena2: " + str(contadorCadena2))


frase1 = str(input("Introduce una cadena: "))
frase2 = str(input("Introduce una cadena: "))
compararASCII(frase1, frase2)
```

### Ejercicio16
```
cadena = str(input("Introduce una cadena: "))
cadenaSeparada = cadena.split(" ")
cadenaNueva = ""
numLetrasMax = 0
palabraMasLarga = ""
for palabra in cadenaSeparada:
    numLetras = 0
    for letra in palabra:
        numLetras += 1
    if(numLetras > numLetrasMax):
        palabraMasLarga = palabra
        numLetrasMax = numLetrasMax
print(palabraMasLarga)
```

### Ejercicio17
```
def separadorMil (num):
    numeros = list(num)
    longitud = 0
    for a in numeros:
        longitud+=1
    numDePuntos = int(longitud / 3)
    indice = 0
    apuntador = longitud - 3
    while(indice < numDePuntos):
        numeros.insert(apuntador, ".")
        indice +=1
        apuntador = apuntador - 3
    nuevoNumero = ""
    for a in numeros:
        nuevoNumero+= a
    print(nuevoNumero)

numero = str(input("Introduce un numero: "))
separadorMil(numero)
```

### Ejercicio18
```
def rotar(cadena, numVeces):
    longitud = 0
    for a in cadena:
        longitud += 1
    if (longitud == numVeces):
        nuevaCadena = cadena
    else:
        if(numVeces > longitud):
            numVeces = numVeces % longitud
        nuevaCadena = cadena[numVeces:] + cadena[:numVeces] 
    print(nuevaCadena)
frase = str(input("Introduce una cadena: "))
numero = int(input("Introduce el n veces a rotar: "))
rotar(frase, numero)
```