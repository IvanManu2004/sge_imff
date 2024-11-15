# Ejemplo de lista de entrada
palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
# Resultado esperado: ['ELEFANTE', 'JIRAFA']
def cinco(palabra):
    if(len(palabra) > 5):
        return palabra
cincoLetras = list(filter(cinco, palabras))
cincoMayus = list(map(lambda mayus: mayus.upper(), cincoLetras))
print(cincoMayus)