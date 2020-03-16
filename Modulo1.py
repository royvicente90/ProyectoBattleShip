def datos():
    print ("==Bienvenido usuario==")
#Necesarios pero Sin Importancia
    gamer = False
    Binario = False
    UserCorrect = False
    UserInvalid = False
    NameCorrect = False
    NameInvalid = False
    UserNameCounter = 0
    #Declaramos username como constante
    global username
    #Caracteres Inválidos para UserName
    AbcInvalid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    #Caracteres Válidos para Name
    AbcValid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    #Números Válidos para Edad
    NumEdad = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200']
    #Números Válidos para Género
    NumGen = ['1', '2']
#Algoritmo
    #Comprobador de UserName
    while UserCorrect == False:
        username = input("Ingrese su nombre de usuario: ")
        for x in username:
            UserNameCounter += 1
            if x in AbcInvalid:
                UserInvalid = True
            else:
                UserCorrect = True
        #Comprobador de Caracteres Validos
        if UserInvalid == True:
            print("Nombre de Usuario Inválido, por favor escriba otro.")
            UserInvalid = False
            UserCorrect = False
        #Comprobador de Length del UserName
        if UserNameCounter >= 30:
            print("Ha excedido el número de caracteres permitido, por favor escriba otro Nombre de Usuario.")
            UserInvalid = False
            UserCorrect = False
    #Comprobador de Name
    while NameCorrect == False:
        nombre = input ("Ingrese su nombre: ")
        for x in nombre:
            if x not in AbcValid:
                NameInvalid = True
            else:
                NameCorrect = True
        #Comprobador de Caracteres Validos
        if NameInvalid == True:
            print("Ha utilizado un caracter invalido como Nombre.\nSe le informa que solo se permite usar caracteres alfabéticos sin caracteres especiales como apóstrofes o acentos.")
            NameInvalid = False
            NameCorrect = False
    #Comprobador de Edad
    while gamer == False:
        edad = input("Ingrese su edad: ")
        if edad not in NumEdad:
            print("Ha introducido un carácter inválido, por favor vuelva a intentarlo.")
        else:
            edad = int(edad)
            if edad >= 5 and edad <= 100:
                gamer = True
            else:
                print("Si usted puede leer y entender éste mensaje, es muy viejo para jugar.\nSi no lo puede leer, ni siquiera sabemos cómo llegó tan lejos")
    #Comprobador de Género
    while Binario == False:
        genero = input("Ingrese su genero: \n1. Femenino \n2. Masculino \n")
        if genero in NumGen:
            genero = int(genero)
            Binario = True
        else:
            print("Le pedimos disculpas al helicoptero de combate Apache u otro tipo de género No Binario.\nSólo podemos aceptar el género con el que usted nació. Cualquier otro género será denegado.")
#Convertir datos en Lista
    m = (username, nombre, edad, genero)
    return(m)
def UserName():
    global username
    return(username)