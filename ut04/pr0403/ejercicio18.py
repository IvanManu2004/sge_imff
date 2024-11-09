listaDeListas = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [8, 5, 3, 9, 5]
]

def resultadosSumas(lista):
    longitudLista = len(lista)
    longitudListas = len(lista[0])
    for a in range(longitudLista):
        print("Suma fila " + str(a) + ": " + str(sumaFilas(a, lista)))
    for b in range(longitudListas):
        print("Suma columna: " + str(b) + ": " + str(sumaColumna(b, lista)))

def sumaFilas(fila, lista):
    resultado = 0
    for a in lista[fila]:
        resultado += a
    return resultado
def sumaColumna(columna, lista):
    resultado = 0
    for b in lista:
        resultado += b[columna]
    return resultado

resultadosSumas(listaDeListas)