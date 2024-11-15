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
