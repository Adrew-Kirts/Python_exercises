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

#prix_a_payer()

#Exo 9


def reduction():
    prix = int(input("Saisir le prix réel: "))

    if 200 < prix < 500:
        print("Vous devez payer: ", (prix - (prix/100)))
    elif 500 < prix < 700:
        print("Vous devez payer: ", (prix - (prix/100*2)))
    elif prix > 700:
        print("Vous devez payer: ", (prix - (prix / 100 * 3)))


#reduction()


#Exo 10

p = int(input("Saissisez la puissance: "))
d = int(input("Saissisez le kilométrage: "))

def kilometres(p, d):
    if p <= 3:
        if d < 5000:
            return d*0.502
        elif 5000 < d <= 20000:
            return (d*0.3) + 1007
        else:
            return d*0.35

    elif p == 4:
        if d < 5000:
            return d*0.575
        elif 5000 < d <= 20000:
            return (d*0.323) + 1262
        else:
            return d*0.387

    elif p == 5:
        if d < 5000:
            return d * 0.603
        elif 5000 < d <= 20000:
            return (d * 0.339) + 1320
        else:
            return d * 0.405

    elif p == 6:
        if d < 5000:
            return d * 0.631
        elif 5000 < d <= 20000:
            return (d * 0.355) + 1382
        else:
            return d * 0.425

    elif p >= 7:
        if d < 5000:
            return d * 0.661
        elif 5000 < d <= 20000:
            return (d * 0.374) + 1435
        else:
            return d * 0.446


print("L'indemnité kilométrique pour", d, "kilomètres, avec une voiture de puissance", p, "est: ", kilometres(p, d))
