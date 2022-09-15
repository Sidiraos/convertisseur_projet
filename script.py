CONSTANTE = 4212.48 #unite1 * constante = unite2
unite1 = "dollars" #1 (unite1) * combien = unite2
unite2 = "ariary"
def demander_type_conversion(unite1 : str , unite2 : str) :
    type_conversion_str = input (f"1-{unite1} --> {unite2}\n2-{unite2} --> {unite1}\n--> ")
    try :
        type_conversion_int = int(type_conversion_str)
    except:
        print('ERREUR : Vous devez rentrer un nombre pour continuer')
        return demander_type_conversion(unite1 , unite2 )
    else:
        if type_conversion_int < 1 or type_conversion_int > 2 :
            print('ERREUR : Vous devez rentrer un nombre entre 1 et 2 pour continuer')
            return demander_type_conversion(unite1 , unite2)
        elif type_conversion_int == 1 :
            print(f'CONVERSION {unite1.upper()} --> {unite2.upper()}')
        else :
            print(f'CONVERSION {unite2.upper()} --> {unite1.upper()}')

    return type_conversion_int

def obtenir_nombre_a_convertir(type_conversion : int, unite1 :str , unite2:str):
    if type_conversion == 1 :
        nombre_a_convertir_str = input(f'entrez le nombre de {unite1}\n--> ') 
    else :
        nombre_a_convertir_str = input(f'entrez le nombre de {unite2}\n--> ')
    try :
        if not (nombre_a_convertir_str == "") :
            nombre_a_convertir = float(nombre_a_convertir_str)
        else :
            nombre_a_convertir = ""
    except:
        print('ERREUR : Vous devez rentrer un nombre pour convertir')
        return obtenir_nombre_a_convertir(type_conversion , unite1 , unite2)

    return nombre_a_convertir

def conversion (type_conversion :int, nombre_a_convertir, CONSTANTE : int , unite1 : str ,unite2 :str) :
    if type_conversion == 1 : #donc pouces vers cm
        resultat = round(nombre_a_convertir * CONSTANTE , 2)
        print(resultat , unite2)
    else : #cm vers pouces
        resultat = round(nombre_a_convertir / CONSTANTE , 2)
        print(resultat , unite1)
        
######################################################################################################################

print(f"Bienvenue dans le programme de Convertion {unite1} vers {unite2} ou \n {unite2} vers {unite1}")
print("Que Souhaitez vous convertir ? \n'Entrez 1 ou 2 selon la conversion de votre choix'")
type_conversion = demander_type_conversion(unite1 , unite2) # pouces en cm ou cm en pouces
print("APPUYEZ ENTRER VIDE POUR QUITTER LE PROGRAMME")
while True :
    nombre_a_convertir= obtenir_nombre_a_convertir(type_conversion , unite1 , unite2) #obtenir le nombre à convertir
    if nombre_a_convertir == "":
        print("fin du programme")
        break
    conversion(type_conversion , nombre_a_convertir , CONSTANTE , unite1 ,unite2) #retourner le resultat obtenu convertion
