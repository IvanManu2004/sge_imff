umbral = float(input("introduce el umbral de salario: "))
diccionario = {
    "Paco":1200.00,
    "Maria":1300.00,
    "Luis":1500.00,
    "Jose":900.00
}
for a in diccionario:
    if(diccionario[a] > umbral):
        print(str(a) + ": " + str(diccionario[a]))