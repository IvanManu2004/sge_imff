cadena = str(input("Introduce una cadena: "))
cadenaSeparada = cadena.split(" ")
nuevaCadena = cadenaSeparada[0]
for palabra in cadenaSeparada[1:]:
    nuevaCadena += palabra.title()
print(nuevaCadena)