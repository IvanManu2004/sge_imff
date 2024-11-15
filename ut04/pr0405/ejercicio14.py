# Ejemplo de lista de entrada
palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]
# Resultado esperado: ['hOLA', 'mUNDO', 'cIELO']
def tres(palabra):
    if(len(palabra) > 3):
        return palabra
tresLetras = list(filter(tres, palabras))
tresMayus = list(map(lambda mayus: mayus[0].lower() + mayus[1:].upper(), tresLetras))
print(tresMayus)