frutas = {
    "Manzana" : 2,
    "Pera" : 3,
    "Platano" : 4,
    "Uva" : 4, 
    "Ciruela" : 2,
    "Higo" : 7,
    "Cereza" : 5,
}
respuesta = str(input("Introduce el nombre de una fruta: "))
resultado = False
for a in frutas:
    if(a == respuesta):
        resultado = True
if(resultado):
    print("El precio de " + respuesta + " es de: " + str(frutas.get(respuesta)) + "€")
else:
    print("La fruta introducida no existe")