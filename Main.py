from Modulo1 import *
from Modulo2 import *
from Modulo3 import *
Lista_Usuarios = []
def Top10():
    x2 = 0
    #Lista de Puntajes
    ListPunt = []
    Temp = []
    print("\\\\\_[[ TOP 10 PUNTUACIONES]]_///")
    print("Formato:")
    print("'Nombre de Usuario', 'Puntuación Máxima', 'Disparos Totales'")
    print();print()
    with open("Puntuaciones.txt", "r") as bd:
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',')
        Temp.append(usuario)
        ListPunt.append(int(usuario[1]))
        ListPunt.sort(reverse = True) 
    for x0 in ListPunt:
        for x in range(len(Temp)):
            if x0 == int(Temp[x][1]):
                x2 += 1
                print(x2,"===",Temp[x])
def Inicio():
    Top10()
    print()
    print()
    print ("\n===== SAMAN-GAMES =====\n")
    opcion = input("Ingrese una opcion \n 1. Jugar \n 2. Estadisticas\n 3. Para Salir del Sistema\n ")
    OpcionesValidas = ["3","1","2"]
    while True:
        #Jugar
        if opcion in OpcionesValidas:
            if opcion == "1":
                Lista_Usuarios = datos()
                print(Lista_Usuarios)
                #Loop volver a jugar
                while opcion == "1":
                    # CleanScreen()
                    Disparo()
                    print()
                    print()
                    opcion = input("Ingrese: \n 1. Si desea volver a jugar \n 2. si desea ver las Estadisticas\n 3. Si desea cerrar el juego\n")
            elif opcion == "2":
                Puntuaciones()
                print()
                print()
                opcion = input("Ingrese: \n 1. Si desea jugar \n 2. si desea volver a ver las Estadisticas\n 3. Si desea cerrar el juego\n")
            elif opcion == "3":
                break
        else:
            print ("Ingrese una opcion valida")
            opcion = input("Ingrese una opcion \n 1. Jugar \n 2. Estadisticas\n 3. Para Salir del Sistema\n ")
Inicio()