diccionario1 = {
    "Pelota":7.53,
    "Camiseta":10.00,
    "Llavero":5.00,
    "Deportivas": 39.99
}
diccionario2 = {
    "Camiseta":9.90,
    "Gafas de Sol":13.00,
    "Llavero":7.20,
    "Planta":23.67
}

nuevoDicc = {}

for a in diccionario1:
    if(diccionario2.get(a, "no") != "no"):
        valor = diccionario1[a] + diccionario2[a]
        nuevoDicc[a] = valor
    else :
        nuevoDicc[a] = diccionario1[a]
for b in diccionario2:
    if(nuevoDicc.get(b, "no") == "no"):
        nuevoDicc[b] = diccionario2[b]
print(nuevoDicc)
