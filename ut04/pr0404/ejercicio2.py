productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

def resultadosSumas(diccionario):
    longitudLista = len(diccionario)
    contador = 0
    print("total categorias: " + str(longitudLista))
    resultado = 0
    for a in diccionario:
        resultado += sumaFilas(diccionario[a])
        print("Total de " + str(a) + ": " + str(sumaFilas(diccionario[a])))    
        contador += 1
    print("Total de productos: " + str(resultado))
        

def sumaFilas(lista):
    resul = 0
    for a in lista:
        resul += 1
    return resul

resultadosSumas(productos)