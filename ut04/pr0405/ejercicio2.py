# Ejemplo de lista de entrada
celsius = [0, 20, 37, 100]
# Resultado esperado: [32.0, 68.0, 98.6, 212.0]
def fahrenheit (numero) :
    return ((numero * 9/5) + 32)
listaFahrenheit = list(map(fahrenheit, celsius))
print(listaFahrenheit)