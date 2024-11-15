# Ejemplo de listas de entrada
lista1 = [1, 2]
lista2 = [3, 4]
# Resultado esperado: [(1, 3), (1, 4), (2, 3), (2, 4)]
resultado = list(map(lambda x: list(map(lambda y: (x, y), lista2)), lista1))
print(resultado)