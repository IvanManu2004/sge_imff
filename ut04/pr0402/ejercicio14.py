cadena = "Hola {nombre} felices {edad} años"
diccionario = {
    "nombre": "Ivan",
    "edad": 20,
}
cadenaSeparada = cadena.split(" ")
cadenaNueva = ""
for palabra in cadenaSeparada:
    if (palabra.count("{") == 1):
        palabraSinCorchetes = palabra[1:-1]
        cadenaNueva += str(diccionario[palabraSinCorchetes])
    else:
        cadenaNueva += palabra
    cadenaNueva += " "
print(cadenaNueva)