

def demander_type_conversion_User() :
    number_str = input ("1-pouces --> cm\n2-cm --> pouces\n--> ")
    try :
        number_int = int(number_str)
    except:
        print('ERREUR : Vous devez rentrer un nombre pour continuer')
        return demander_type_conversion_User()
    else:
        if number_int < 1 or number_int > 2 :
            print('ERREUR : Vous devez rentrer un nombre entre 1 et 2 pour continuer')
            return demander_type_conversion_User()
        elif number_int == 1 :
            print('pouces --> cm')
            return number_int
        else :
            print('cm --> pouces')
            return number_int

def obtenir_nombre_convertir(number_int):
    if number_int == 1 :
        nombre_convert_str = input('entrez le nombre de pouces\n--> ')
        return nombre_convert_str

    elif number_int == 2 :
        nombre_convert_str = input('entrez le nombre de cm\n--> ')
        return nombre_convert_str

def conversion (number_for_convert_str , number_int) :
    try :
       number_for_convert = float(number_for_convert_str)
       #number_for_convert = int (number_for_convert_float) 
    except:
        print('ERREUR : Vous devez rentrer un nombre pour convertir')
        return obtenir_nombre_convertir(number_int)
    else :
        if number_int == 1 : #donc pouces vers cm
            resultat = number_for_convert * 2.54
            afficher_resultat = str(resultat) + ' cm'
            return afficher_resultat
        elif number_int == 2 : #cm vers pouces
            resultat = number_for_convert * 0.394
            afficher_resultat = str(resultat) + ' pouces'
            return afficher_resultat


def convertir() :
    while True :
        number_for_convert_str = obtenir_nombre_convertir(number_int) #obtenir le nombre à convertir
        if number_for_convert_str == "":
            return
        resultat = conversion(number_for_convert_str , number_int) #retourner le resultat obtenu convertion
        print(resultat)


print("Bienvenue dans le programme de Convertion pouces vers cm ou \n cm vers pouces")
print("Que Souhaitez vous convertir ? \n'Entrez 1 ou 2 selon la conversion de votre choix'")
print()
number_int = demander_type_conversion_User() # pouces en cm ou cm en pouces
print()

convertir()

