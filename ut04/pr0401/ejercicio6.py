cantidad = int(input("Introduce el valor: "))
unidadQueEsta = str(input("Introduce la unidad en que esta: "))
unidadQueSePasa = str(input("Introduce la unidad a la que lo quieres pasar: "))
num = 0
match unidadQueEsta:
    case "mm":
        match unidadQueSePasa:
            case "cm":
                num = cantidad / 10
            case "m":
                num = cantidad / 1000
            case "km":
                num = cantidad / 1000000
    case "cm":
        match unidadQueSePasa:
            case "mm":
                num = cantidad * 10
            case "m":
                num = cantidad / 100
            case "km":
                num = cantidad / 100000
    case "m":
        match unidadQueSePasa:
            case "mm":
                num = cantidad * 1000
            case "cm":
                num = cantidad * 100
            case "km":
                num = cantidad / 1000
    case "km":
        match unidadQueSePasa:
            case "mm":
                num = cantidad * 1000000
            case "cm":
                num = cantidad * 100000
            case "m":
                num = cantidad * 1000
print("el numero " + str(cantidad) + " que esta en " + unidadQueEsta + " da como resultado " + str(num) + unidadQueSePasa)
