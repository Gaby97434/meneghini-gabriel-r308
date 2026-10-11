import random

def demander_entier(message):
    # Redemande tant que la saisie n'est pas un entier
    while True:
        try:
            return int(input(message))  # return dans le try : on ne sort que si la conversion a réussi
        except ValueError:
            print("Tape un nombre entier pas une lettre ou je ne sais quoi ")

def jouer_devine(mini, maxi):
    # Une partie : renvoie True si gagné, False sinon
    secret = random.randint(mini, maxi)  # nombre secret entre mini et maxi avec les bornes incluses
    essais = 0
    joker_utilise = False

    while essais < 10:  # tant qu'il reste des essais
        reponse = input(f"Le nombre entre {mini} et {maxi} : ")
        try:
            nombre = int(reponse)
        except ValueError:  # la saisie n'est pas un nombre
            if not joker_utilise:
                joker_utilise = True  # premier essai invalide : gratuit
                print("C'est un chiffre à trouver hein...")
            else:
                essais += 1
                print("Tu perds donc un essai désolé...")
            continue  # tour suivant, sans comparer
        essais += 1  # essai valide : il compte
        if nombre < secret:
            print("Trop petit !")
        elif nombre > secret:
            print("Trop grand !")
        else:
            print("Gagné ! Bien joué !")
            return True  # quitte tout de suite la boucle et la fonction : plus besoin de break

    print("Perdu, le nombre était :", secret, "\nRETENTE !")
    return False

while True:
    mini = demander_entier("Borne minimale : ")
    maxi = demander_entier("Borne maximale : ")
    while mini >= maxi:  # randint plante si mini > maxi, et mini == maxi rendrait le jeu trivial
        print("La borne maximale doit être plus grande que la minimale")
        maxi = demander_entier("Borne maximale : ")

    jouer_devine(mini, maxi)

    if input("Rejouer ? (o/n) ").lower() != "o":  # Une partie par tour de boucle, on rejoue tant que le joueur répond "o"
        break