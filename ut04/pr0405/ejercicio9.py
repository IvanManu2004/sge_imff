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