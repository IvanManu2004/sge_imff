from functools import reduce
# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5]
# Resultado esperado: 15
suma = reduce(lambda acumulador, valor: acumulador + valor, numeros)
print(suma)
