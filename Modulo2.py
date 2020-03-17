from random import *
from Modulo1 import *
import os
tablero = [["0A", "0B", "0C", "0D", "0E", "0F", "0G", "0H", "0I", "0J"], ["1A", "1B", "1C", "1D", "1E", "1F", "1G", "1H", "1I", "1J"], ["2A", "2B", "2C", "2D", "2E", "2F", "2G", "2H", "2I", "2J"], ["3A", "3B", "3C", "3D", "3E", "3F", "3G", "3H", "3I", "3J"], ["4A", "4B", "4C", "4D", "4E", "4F", "4G", "4H", "4I", "4J"], ["5A", "5B", "5C", "5D", "5E", "5F", "5G", "5H", "5I", "5J"],["6A", "6B", "6C", "6D", "6E", "6F", "6G", "6H", "6I", "6J"],["7A", "7B", "7C", "7D", "7E", "7F", "7G", "7H", "7I", "7J"],["8A", "8B", "8C", "8D", "8E", "8F", "8G", "8H", "8I", "8J"],["9A", "9B", "9C", "9D", "9E", "9F", "9G", "9H", "9I", "9J"]]
tablero_mod = []
tablero_modded = [[' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O'], [' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O', ' O']]
Ships = []
def CleanScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def Puntaje():
  global DispTotal
  global PuntosTotales  
  global username
  with open("Puntuaciones.txt", "a+") as bd:
      bd.write("{},{},{}\n".format(username, PuntosTotales, DispTotal))
  print('Sus puntajes han sido guardados exitosamente')
def GameInit(tablero_mod):
    #TABLERO
  for x in tablero:
    tablero_mod.append(x)
  for y in tablero_mod:
    print(y)
  print()
  for z in tablero_modded:
    print(z)
#Funcion Vertical u Horizontal
def verhor():
  ver = False
  aux = randint(0,1)
  if aux == 0:
    ver = False
  else:
    ver = True
  return ver
#Funcion Barcos de 1 espacio 
def barquito1():
  x = randint(0,9)
  y = randint(0,9)
  return(x,y)
#Funcion Barco de 3 espacios
def barquito3():
  x,y = barquito1()
  #Caso Vertical u Horizontal con Caso de Limites
  if  verhor() == True:
    if x == 9:
      x0 = 9
      x2 = 8
      x3 = 7
    elif x == 0:
      x0 = 0
      x2 = 1
      x3 = 2
    else:
      x0 = x
      x2 = x + 1
      x3 = x - 1
    y0 = y
    y2 = y
    y3 = y
  else:
    if y == 9:
      y0 = 9
      y2 = 8
      y3 = 7
    elif y == 0:
      y0 = 0
      y2 = 1
      y3 = 2
    else:
      y0 = y
      y2 = y + 1
      y3 = y - 1
    x0 = x
    x2 = x
    x3 = x
  return(x0,x2,x3,y0,y2,y3)
#Funcion Barco de 2 espacios    
def barquito2():
  x,y = barquito1()
  #Caso Vertical u Horizontal con Caso de Limites
  if  verhor() == True:
    if x == 9:
      x = 9
      x2 = 8
    elif x == 0:
      x = 0
      x2 = 1
    else:
      x = x
      x2 = x - 1
    y = y
    y2 = y
  else:
    if y == 9:
      y = 9
      y2 = 8
    elif y == 0:
      y = 0
      y2 = 1
    else:
      y = y
      y2 = y - 1
    x = x
    x2 = x
  return(x,x2,y,y2)
def Disparo():
  print("Atención, la flota enemiga está conformada por: \n- Un (1) buque de tres (3) posiciones: Este buque tiene la capacidad de aterrizar helicópteros en él para el transporte de tropas.\n- Un (1) buque de dos (2) posiciones: Tiene la capacidad de comunicarse con tierra y los otros miembros de la flota. \n- Cuatro (4) submarinos de una sola posición cada uno: Tiene la capacidad de poder sumergirse y emerger del agua.")
  ShipAlive = True
  #Variables sin Importancia
  Barco2rpt = True
  Sub1rpt = True
  Sub2rpt = True
  Sub3rpt = True
  Sub4rpt = True
  Winner = []
  Temporal = []
  InstaWin = "InstaWin"
  #Set Variables de Puntuaciones como Globales
  global DispAcer
  global DispErr
  global DispRpt
  global DispTotal
  global PuntosTotales  
  global username
  #Variables de Puntuaciones
  DispAcer = 0
  DispErr = 0
  DispRpt = 0
  DispTotal = 0
  PuntosTotales = 0
  username = UserName()
  #Variables Posiciones de Barcos
  Barco31 = []
  Barco32 = []
  Barco33 = []
  Barco21 = []
  Barco22 = []
  Sub1 = []
  Sub2 = []
  Sub3 = []
  Sub4 = []
  Posiciones = []

  #Generacion Posiciones de Barcos
  B3x,B3x1,B3x2,B3y,B3y1,B3y2 = barquito3()

  Barco31.append(B3x);Barco31.append(B3y)
  Barco32.append(B3x1);Barco32.append(B3y1)
  Barco33.append(B3x2);Barco33.append(B3y2)
  Posiciones.append(Barco31)
  Posiciones.append(Barco32)
  Posiciones.append(Barco33)

  while Barco2rpt == True:
    B2x,B2x1,B2y,B2y1 = barquito2()
    Barco21.append(B2x);Barco21.append(B2y)
    Barco22.append(B2x1);Barco22.append(B2y1)  
    if Barco21 in Posiciones or Barco22 in Posiciones:
      Barco21.clear()
      Barco22.clear()
    else:
      Posiciones.append(Barco21)
      Posiciones.append(Barco22)
      Barco2rpt = False

  while Sub1rpt == True:
    S1x,S1y = barquito1()
    Sub1.append(S1x);Sub1.append(S1y)
    if Sub1 in Posiciones:
      Sub1.clear()
    else:
      Posiciones.append(Sub1)
      Sub1rpt = False
    
  while Sub2rpt == True:
    S2x,S2y = barquito1()
    Sub2.append(S2x);Sub2.append(S2y)
    if Sub2 in Posiciones:
      Sub2.clear()
    else:
      Posiciones.append(Sub2)
      Sub2rpt = False

  while Sub3rpt == True:
    S3x,S3y = barquito1()
    Sub3.append(S3x);Sub3.append(S3y)
    if Sub3 in Posiciones:
      Sub3.clear()
    else:
      Posiciones.append(Sub3)
      Sub3rpt = False

  while Sub4rpt == True:
    S4x,S4y = barquito1()
    Sub4.append(S4x);Sub4.append(S4y)
    if Sub4 in Posiciones:
      Sub4.clear()
    else:
      Posiciones.append(Sub4)
      Sub4rpt = False

  print(Barco31,Barco32,Barco33)
  print(Barco21,Barco22)
  print(Sub1);print(Sub2);print(Sub3);print(Sub4)
  #======================LOOP DE JUEGO================================
  while ShipAlive:
    tablero_mod.clear()
    GameInit(tablero_mod)
    CoordExist = False
    Repeat = False
    print(Posiciones)
    m = input("Ingrese la coordenada en la que desea disparar: ").upper()
    if m == InstaWin.upper():
      ShipAlive = False      
    for x in range (len(tablero_mod)):
      for y in range (len(tablero_mod[x])):
          if m == tablero_mod[x][y]:
            Temporal.append(x)
            Temporal.append(y)
            if tablero_modded[x][y] == " F" or tablero_modded[x][y] == " X":
              DispRpt += 1
              print("Ese disparo ya lo hiciste")
              Repeat = True
              Temporal.clear()
            while Repeat == False:
              if Temporal in Posiciones:
                Posiciones.remove(Temporal)
                print("Le diste a algo!")
                Temporal.clear()
                tablero_modded[x][y] = " F"
                DispAcer += 1
                if Posiciones == Winner:
                      ShipAlive = False
              else:
                tablero_modded[x][y] = " X"
                DispErr += 1
                Temporal.clear()
              break
            CoordExist = True
    if CoordExist == False and Repeat == False:      
      print("Introdujo una coordenada inválida, por favor reintente.")
    print()
    print()
  PuntosTotales = (DispAcer * 10) - (DispErr * 2)
  DispTotal = DispAcer + DispErr
  print("=========== FELICIDADES, HAS GANADO!!! ===========")
  if DispTotal == 9:
    print("-¿Eres un Robot? Lo que acabas de hacer es poco probable…")
  if DispTotal < 45:
    print("-Excelente Estrategia.")
  if DispTotal >= 45 and DispTotal <= 70:
    print("-Buena Estrategia; pero hay que mejorar.")
  if DispTotal > 70:
    print("-Considérese Perdedor, tiene que mejorar notablemente")
  print()
  print()
  print("[[\_,",username,"_/]]")
  print("-Con un total de",DispTotal,"disparos.")
  print("-Tienes un total de",PuntosTotales,"puntos")
  print("-Has acertado",DispAcer,"disparos.")
  print("-Te has equivocado en",DispErr,"disparos.")
  print("-Has intentado repetir un tiro anterior",DispRpt,"veces.")
  print()
  for z in tablero_modded:
    print(z)
  print()
  Puntaje()