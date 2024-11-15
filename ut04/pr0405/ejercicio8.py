# Ejemplo de listas de entrada
lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
# Resultado esperado: [3, 4, 5]

numerosComunes = filter(lambda x: x in lista2, lista1)
print(list(numerosComunes))