def Puntuaciones():
    try:
  #Que rango de edad están los usuarios que más juegan
        #Variables
        e5a18 = 0
        e19a45 = 0
        e46a60 = 0
        e61a100 = 0
        TotalDispSum = 0
        CountDisp = 0
        NotEmpty = True
        #Organizador (¿Cual es el mayor?)
        Organizer = []
        #Lector de Base de Datos
        with open("BD.txt", "r") as bd:
            datos = bd.readlines()
        for dato in datos:
            usuario = dato[:-1].split(',')
            if int(usuario[2]) >= 5 and int(usuario[2]) <= 18:
                e5a18 += 1
            if int(usuario[2]) >= 19 and int(usuario[2]) <= 45:
                e19a45 += 1
            if int(usuario[2]) >= 46 and int(usuario[2]) <= 60:
                e46a60 += 1
            if int(usuario[2]) >= 61 and int(usuario[2]) <= 100:
                e61a100 += 1
        if e5a18 == 0 and e19a45 == 0 and e46a60 == 0 and e61a100 == 0:
            NotEmpty = False
        while NotEmpty == True:
            Organizer.append(e5a18);Organizer.append(e19a45);Organizer.append(e46a60);Organizer.append(e61a100)
            Organizer.sort(reverse = True)
            print(("Entre los usuarios registrados:\nHay {} jugadores comprendidos entre 5 y 18 años.\nHay {} jugadores comprendidos entre 19 y 45 años.\nHay {} jugadores comprendidos entre 46 y 60 años.\nHay {} jugadores comprendidos entre 61 y 100 años.").format(e5a18,e19a45,e46a60,e61a100))
            print()
            if Organizer[0] == e5a18:
                print("Siendo el rango de edades que mas usuarios de éste juego tienen, de 5 a 18 años.")
            if Organizer[0] == e19a45:
                print("Siendo el rango de edades que mas usuarios de éste juego tienen, de 19 a 45 años.")
            if Organizer[0] == e46a60:
                print("Siendo el rango de edades que mas usuarios de éste juego tienen, de 46 a 60 años.")
            if Organizer[0] == e61a100:
                print("Siendo el rango de edades que mas usuarios de éste juego tienen, de 61 a 100 años.")
            print()
            print()
            break
        #Cantidad total de puntos en partidas por género
            #Variables
        UyG = []
        UyGTemp = []
        UyP = []
        UyPTemp = []
        ListHombres = []
        ListMujeres = []
        UserTemp = []
        PuntH = 0
        PuntM = 0
            #Invocación de Datos
        for dato3 in datos:
            usuario = dato3[:-1].split(',')
            UyGTemp = [usuario[0],usuario[3]]
            UyG.append(UyGTemp)
        with open("Puntuaciones.txt", "r") as bd2:
            datos2 = bd2.readlines()
        for dato3 in datos2:
            usuario3 = dato3[:-1].split(',')
            UyPTemp = [usuario3[0],usuario3[1]]
            UyP.append(UyPTemp)
        for x5 in range(len(UyG)):
            for x6 in range(len(UyP)):
                if UyG[x5][0] == UyP[x6][0]:
                    if UyG[x5][1] == '1':
                        UserTemp = [UyG[x5][0], int(UyP[x6][1])]
                        ListMujeres.append(UserTemp)
                    if UyG[x5][1] == '2':
                        UserTemp = [UyG[x5][0], int(UyP[x6][1])]
                        ListHombres.append(UserTemp)
            #Info General y Selector
        for PH1 in range(len(ListHombres)):
            PH = ListHombres[PH1][1]
            PuntH = PuntH + int(PH)
        print("El total de Puntos para el género Masculino es de",PuntH,"puntos.")
        for PM1 in range(len(ListMujeres)):
            PM = ListMujeres[PM1][1]
            PuntM = PuntM + int(PM)
        print("El total de Puntos para el género Femenino es de",PuntM,"puntos.")
        print()
        print("Siendo sumados en el total para Masculinos:")
        print(ListHombres)
        print("Y siendo sumados en el total para Femeninos:")
        print(ListMujeres)

            #Total de Puntos para Femeninos
        print();print()
        #Promedio de disparos realizados para ganar
        #Lector de Puntuaciones
        for dato2 in datos2:
            usuario2 = dato2[:-1].split(',')
            CountDisp = CountDisp + int(usuario2[2])
            TotalDispSum += 1
        CountDisp = CountDisp/TotalDispSum
        print("Contando todos los registros, hasta ahora hay un promedio necesario para ganar de",CountDisp,"disparos.")
    except ZeroDivisionError:
        print("Todavía no se encuentran puntuaciones registradas")