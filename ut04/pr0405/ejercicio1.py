# Ejemplo de lista de entrada
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Resultado esperado: [2, 4, 6, 8, 10]
def comprobarPares(numero):
    return numero % 2 == 0
nuevaLista = list(filter(comprobarPares, numeros))
print(nuevaLista)