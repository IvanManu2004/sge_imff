from random import *

ganadasUsuario = 0
ganadasMaquina = 0
while (ganadasUsuario < 5 and ganadasMaquina < 5):
    entradaUsuario = str(input("Introduce piedra | papel | tijeras | lagarto | spock "))
    numRandom = randint(1, 5)
    if (numRandom == 1):
        entradaMaquina = "piedra"
    elif (numRandom == 2):
        entradaMaquina = "papel"
    elif (numRandom == 3):
        entradaMaquina = "tijeras"
    elif (numRandom == 4):
        entradaMaquina = "lagarto"
    elif (numRandom == 5):
        entradaMaquina = "spock"
    
    if (entradaUsuario == "tijeras" and (entradaMaquina == "lagarto" or entradaMaquina == "papel")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == "piedra" and (entradaMaquina == "lagarto" or entradaMaquina == "tijeras")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == "papel" and (entradaMaquina == "piedra" or entradaMaquina == "spock")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == "lagarto" and (entradaMaquina == "spock" or entradaMaquina == "papel")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == "spock" and (entradaMaquina == "piedra" or entradaMaquina == "tijeras")):
        ganadasUsuario += 1
        print (entradaUsuario + " gana a " + entradaMaquina)
        print ("Usuario suma un punto ")
    elif (entradaUsuario == entradaMaquina):
        print ("Empate ")
    else :
        ganadasMaquina += 1
        print (entradaMaquina + " gana a " + entradaUsuario)
        print ("Maquina suma un punto: ")

print ("Puntos usuario: " + str(ganadasUsuario) + " | Puntos maquina: " + str(ganadasMaquina))