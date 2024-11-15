from functools import reduce
# Ejemplo de listas de entrada
lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']
# Resultado esperado: ['a', 'b', 'c', 'x', 'y', 'z']

listaConjunta = reduce(lambda listaAcumuladora, elemento: listaAcumuladora + [elemento], lista1 + lista2, [])
print(listaConjunta)