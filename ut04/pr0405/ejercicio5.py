from functools import reduce
# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5, 6]
# Resultado esperado: 48 (producto de 2, 4 y 6)
def par(num):
    return num % 2 == 0
pares = list(filter(par, numeros))
paresSumados = reduce(lambda acumulador, valor: acumulador * valor, pares)
print(paresSumados)