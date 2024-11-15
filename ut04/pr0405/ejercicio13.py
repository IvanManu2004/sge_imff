from functools import reduce
# Ejemplo de funciones y lista de entrada
funciones = [lambda x: x*2, lambda x: x+3, lambda x: x-1]
numeros = [1, 2, 3]
# Resultado esperado: [((1*2)+3)-1, ((2*2)+3)-1, ((3*2)+3)-1] -> [4, 6, 8]
resultado = [reduce(lambda acumulador, funcion: funcion(acumulador), funciones, num) for num in numeros]
print(resultado)