## [Unidad 4](../index.md)
# Practica 5


### Ejercicio1
```
# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Resultado esperado: [2, 4, 6, 8, 10]
def comprobarPares(numero):
    return numero % 2 == 0
nuevaLista = list(filter(comprobarPares, numeros))
print(nuevaLista)
```


### Ejercicio2
```
# Ejemplo de lista de entrada
celsius = [0, 20, 37, 100]
# Resultado esperado: [32.0, 68.0, 98.6, 212.0]
def fahrenheit (numero) :
    return ((numero * 9/5) + 32)
listaFahrenheit = list(map(fahrenheit, celsius))
print(listaFahrenheit)
```


### Ejercicio3
```
from functools import reduce
# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5]
# Resultado esperado: 15
suma = reduce(lambda acumulador, valor: acumulador + valor, numeros)
print(suma)

```


### Ejercicio4
```
# Ejemplo de lista de entrada
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
# Resultado esperado: ['ELEFANTE', 'JIRAFA']
def cinco(palabra):
    if(len(palabra) > 5):
        return palabra
cincoLetras = list(filter(cinco, palabras))
cincoMayus = list(map(lambda mayus: mayus.upper(), cincoLetras))
print(cincoMayus)
```


### Ejercicio5
```
from functools import reduce
# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5, 6]
# Resultado esperado: 48 (producto de 2, 4 y 6)
def par(num):
    return num % 2 == 0
pares = list(filter(par, numeros))
paresSumados = reduce(lambda acumulador, valor: acumulador * valor, pares)
print(paresSumados)
```


### Ejercicio6
```
from functools import reduce
# Ejemplo de lista de entrada
numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]
# Resultado esperado: 30 (suma de 2, 7, 10, 3, y 8)
def esPositivo(num):
    if(num > 0):
        return True
    else :
        return False
    
positivos = map(lambda sublista: filter(esPositivo, sublista), numeros)
listasSumadas = map(lambda sublista: reduce(lambda x, y: x + y, sublista), positivos)
sumaTotal = reduce(lambda x, y: x + y, listasSumadas)

print(sumaTotal)

```


### Ejercicio7
```
from functools import reduce
# Ejemplo de texto de entrada
texto = "Hola hola mundo mundo cruel"
# Resultado esperado: {'hola': 2, 'mundo': 2, 'cruel': 1}
palabras = map(str.lower, texto.split())
def contarFrecuencia(diccionario, palabra):
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1
    return diccionario
frecuencia = reduce(contarFrecuencia, palabras, {})
print(frecuencia)
```


### Ejercicio8
```
# Ejemplo de listas de entrada
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
# Resultado esperado: [3, 4, 5]

numerosComunes = filter(lambda x: x in lista2, lista1)
print(list(numerosComunes))
```


### Ejercicio9
```
from functools import reduce
# Ejemplo de lista de entrada
palabras = ["sol", "luna", "estrella", "cielo", "mar"]
# Resultado esperado: {3: ['sol', 'mar'], 4: ['luna', 'cielo'], 8: ['estrella']}
def contarFrecuencia(diccionario, palabra):
    if len(palabra) in diccionario:
        diccionario[len(palabra)] = diccionario[len(palabra)], palabra
    else:
        diccionario[len(palabra)] = palabra
    return diccionario
frecuencia = reduce(contarFrecuencia, palabras, {})
print(frecuencia)
```


### Ejercicio10
```
from functools import reduce
# Ejemplo de listas de entrada
lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']
# Resultado esperado: ['a', 'b', 'c', 'x', 'y', 'z']

listaConjunta = reduce(lambda listaAcumuladora, elemento: listaAcumuladora + [elemento], lista1 + lista2, [])
print(listaConjunta)
```


### Ejercicio11
```
# Ejemplo de lista de entrada
alumnos = [("Ana", 4), ("Bruno", 7), ("Clara", 5), ("David", 8)]
# Resultado esperado: ['Bruno', 'Clara', 'David']
alumnosAprobados = filter(lambda x : x[1] >= 5, alumnos)
nombres = list(map(lambda x: x[0], alumnosAprobados))
print(nombres)
```


### Ejercicio12
```
# Ejemplo de listas de entrada
lista1 = [1, 2]
lista2 = [3, 4]
# Resultado esperado: [(1, 3), (1, 4), (2, 3), (2, 4)]
resultado = list(map(lambda x: list(map(lambda y: (x, y), lista2)), lista1))
print(resultado)
```


### Ejercicio13
```
from functools import reduce
# Ejemplo de funciones y lista de entrada
funciones = [lambda x: x*2, lambda x: x+3, lambda x: x-1]
numeros = [1, 2, 3]
# Resultado esperado: [((1*2)+3)-1, ((2*2)+3)-1, ((3*2)+3)-1] -> [4, 6, 8]
resultado = [reduce(lambda acumulador, funcion: funcion(acumulador), funciones, num) for num in numeros]
print(resultado)
```


### Ejercicio14
```
# Ejemplo de lista de entrada
palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]
# Resultado esperado: ['hOLA', 'mUNDO', 'cIELO']
def tres(palabra):
    if(len(palabra) > 3):
        return palabra
tresLetras = list(filter(tres, palabras))
tresMayus = list(map(lambda mayus: mayus[0].lower() + mayus[1:].upper(), tresLetras))
print(tresMayus)
```
