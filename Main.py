from Modulo1 import *
from Modulo2 import *
Lista_Usuarios = []
def Inicio():
    print ("\n===== SAMAN-GAMES =====\n")
    opcion = input("Ingrese una opcion \n 1. Jugar \n 2. Estadisticas\n ")
    if opcion == "1":
        Lista_Usuarios = datos()
        CleanScreen()
        print(Lista_Usuarios)
        Disparo()

    elif opcion == "2":
        print("In Process")

    else:
        print ("Ingrese una opcion valida")
Inicio()