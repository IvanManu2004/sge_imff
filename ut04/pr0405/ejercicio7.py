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