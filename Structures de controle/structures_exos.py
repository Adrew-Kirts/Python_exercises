#Exo 1
def array_creation():
    user_array = []
    for _ in range(3):
        element = int(input("Enter element: "))
        user_array.append(element)
    return user_array


def biggest_number(a):
    if a[0] > a[1] and a[0] > a[2]:
        print("The biggest value in the list is ", a[0])
    elif a[1] > a[0] and a[1] > a[2]:
        print("The biggest value in the list is ", a[1])
    else:
        print("The biggest value in the list is ", a[2])


#biggest_number(array_creation())

#Exo 2

def modulo(n):
    while n >= 2:
        n -= 2
    return n


def even_or_not():
    n = int(input("Enter a number: "))
    if modulo(n) == 0:
        print(n, "is an even number")
    else:
        print(n, "is an uneven number")


#even_or_not()


#Exo 3

def modulo_two(n, o):
    while n >= o:
        n -= o
    return n
def seven_or_thirteen():
    n = int(input("Enter a number: "))
    if modulo_two(n, 7) == 0 and modulo_two(n, 13) == 0:
        print(n, "can be divided by 7 and 13")
    else:
        print(n, "can't be divided by 7 and 13")


#seven_or_thirteen()

#Exo 4

def bac():
    n = int(input("Enter a number: "))
    match n:
        case 11:
            print("Obtenu sans mention")
        case 12 | 13:
            print("Assez bien")
        case 14 | 15 | 16 | 17 | 18 | 19 | 20:
            print("Bien")
        case _:
            print("Recalé")

#bac()


#Exo 5



def bissextile(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        #print(n,"est une année bissextile")
        return True

#bissextile()

#Exo 6


def year_month():
    y = int(input("Enter a year: "))
    m = input("Enter a month: ")

    if bissextile(y):
        match m:

            case "fevrier":
                print("Le mois de", m, "de l'an", y, "contient 29 jours")
            case "janvier" | "mars" | "mai" | "juillet" | "aout" | "octobre" | "decembre":
                print("Le mois de", m, "de l'an", y, "contient 31 jours")
            case "avril" | "juin" | "septembre" | "novembre":
                print("Le mois de", m, "de l'an", y, "contient 30 jours")

    else:
        match m:

            case "fevrier":
                print("Le mois de", m, "de l'an", y, "contient 28 jours")
            case "janvier" | "mars" | "mai" | "juillet" | "aout" | "octobre" | "decembre":
                print("Le mois de", m, "de l'an", y, "contient 31 jours")
            case "avril" | "juin" | "septembre" | "novembre":
                print("Le mois de", m, "de l'an", y, "contient 30 jours")

#year_month()

#Exo 7

def voyelle_ou_pas():
    letter = ""

    while len(letter) != 1:
        letter = input("saisir une lettre: ")

    if letter in ("a","e","i","o","u","y"):
        print(letter, "est une voyelle")
    else:
        print(letter, "n'est pas une voyelle")

#voyelle_ou_pas()

#Exo 8

def prix_a_payer():
    prix = int(input("Saisir le prix réel: "))

    if prix > 200:
        print("Vous devez payer: ",(prix - (prix/100)))
    else:
        print("Vous devez payer: ",prix)

prix_a_payer()

#Exo 9


