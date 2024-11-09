## [Unidad 4](../index.md)
# Practica 1
### Ejercicio1
```
numero = input("introduce un numero ")
while (not numero.isdigit()):
    numero = input("introduce un numero ")
print(numero)
```

### Ejercicio2
```
n = int(input("Introduce un numero"))
k = int(input("Introduce el numero de veces que lo quieres multiplicar"))
index = 0
while(int(index) <= int(k)):
    index += 1
    numMultiplicado = int(n)*index
    print(str(n) + " * " + str(index) + " = " + str(numMultiplicado))
    

```

### Ejercicio3
```
longitudBase = int(input("Introduce un numero"))
caracter = "*"
dibujar = ""
index = 0
while (index < longitudBase):
    dibujar += caracter
    print(dibujar)
    index += 1
    
```

### Ejercicio4
```
longitudBase = int(input("Introduce un numero"))
if (longitudBase % 2 == 0):
    while (longitudBase % 2 == 0) :
        longitudBase = int(input("Introduce un numero impar"))

mitadNumero = (longitudBase + 1) / 2
espacio = ""
caracter = "*"
caracteres = ""
imprimir = ""
index = 0
while (index < mitadNumero):
    i = index
    espacio = ""
    while (i < (mitadNumero - 1)):
        espacio += " "
        i += 1
    if (index == 0):
        caracteres += caracter
    else :
        caracteres += caracter + caracter
    imprimir = espacio + caracteres
    print(imprimir)
    index += 1
```

### Ejercicio5
```
import math
index = 0
numMax = 0
numMin = math.inf
while (index < 5):
    num = int(input("introduce un numero"))
    if (num >= numMax):
        numMax = num
    if (num < numMin):
        numMin = num
    index += 1
print("El numero mayor es " + str(numMax) + " y el numero minimo es " + str(numMin))

```

### Ejercicio6
```
cantidad = int(input("Introduce el valor: "))
unidadQueEsta = str(input("Introduce la unidad en que esta: "))
unidadQueSePasa = str(input("Introduce la unidad a la que lo quieres pasar: "))
num = 0
match unidadQueEsta:
    case "mm":
        match unidadQueSePasa:
            case "cm":
                num = cantidad / 10
            case "m":
                num = cantidad / 1000
            case "km":
                num = cantidad / 1000000
    case "cm":
        match unidadQueSePasa:
            case "mm":
                num = cantidad * 10
            case "m":
                num = cantidad / 100
            case "km":
                num = cantidad / 100000
    case "m":
        match unidadQueSePasa:
            case "mm":
                num = cantidad * 1000
            case "cm":
                num = cantidad * 100
            case "km":
                num = cantidad / 1000
    case "km":
        match unidadQueSePasa:
            case "mm":
                num = cantidad * 1000000
            case "cm":
                num = cantidad * 100000
            case "m":
                num = cantidad * 1000
print("el numero " + str(cantidad) + " que esta en " + unidadQueEsta + " da como resultado " + str(num) + unidadQueSePasa)

```

### Ejercicio7
```
from random import *
num = randint(1, 100)
numUsuario = int(input("Introduce un numero: ")) 
while (numUsuario!= num):
    if (numUsuario < num):
        print("El numero es mas grande")
    else:
        print("El numero es mas pequeño")
    numUsuario = int(input("Introduce un numero: ")) 
print("Has acertado el numero")
```

### Ejercicio8
```
from random import *

ganadasUsuario = 0
ganadasMaquina = 0
while (ganadasUsuario < 5 and ganadasMaquina < 5):
    entradaUsuario = str(input("Introduce piedra | papel | tijeras | lagarto | spock "))
    numRandom = randint(1, 5)
    if (numRandom == 1):
        entradaMaquina = "piedra"
    elif (numRandom == 2):
        entradaMaquina = "papel"
    elif (numRandom == 3):
        entradaMaquina = "tijeras"
    elif (numRandom == 4):
        entradaMaquina = "lagarto"
    elif (numRandom == 5):
        entradaMaquina = "spock"
    
    if (entradaUsuario == "tijeras" and (entradaMaquina == "lagarto" or entradaMaquina == "papel")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == "piedra" and (entradaMaquina == "lagarto" or entradaMaquina == "tijeras")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == "papel" and (entradaMaquina == "piedra" or entradaMaquina == "spock")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == "lagarto" and (entradaMaquina == "spock" or entradaMaquina == "papel")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == "spock" and (entradaMaquina == "piedra" or entradaMaquina == "tijeras")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == entradaMaquina):
        print ("Empate ")
    else :
        ganadasMaquina += 1
        print (entradaMaquina + " gana a " + entradaUsuario)
        print ("Maquina suma un punto: ")

print ("Puntos usuario: " + str(ganadasUsuario) + " | Puntos maquina: " + str(ganadasMaquina))
```

### Ejercicio9
```
numMax = int(input("Introduce el n primeros numeros para la secuencia: "))
numAnterior = 0
guardarNum = 0
numAnteriorAnterior = 0
num = 0
index = 0
while (index < numMax):
    num = numAnterior + numAnteriorAnterior
    print(num)
    numAnteriorAnterior, numAnterior = numAnterior, num
    index += 1
    if(index == 1 and (numAnterior == 0 and numAnteriorAnterior == 0)):
        numAnterior = 1
    
```