import random

secret = random.randint(1, 100)  # Initialisation du nombre secret entre 1 et 100 grâce à randint
essais = 0
joker_utilise = False
gagner = False

while essais < 10: # Tant qu'il reste des essais (moins de 10)
    reponse = input("Ton nombre : ")
    try:
        nombre = int(reponse)
    except ValueError: # Cas où si la valeur rentrée n'est pas numérique
        if not joker_utilise : # Vérifie si le joker est utilisé ou non 
            joker_utilise = True
            print("C'est un chiffre à trouver hein...") # Cas où si le Joker n'est pas utilisé, le nombre d'essai n'augmente pas 
        else:
            essais += 1
            print("Tu perds donc un essai désolé...") # Cas si le Joker a déjà été utilisé, le nombre d'essai augmente
        continue # Passe directement au tour suivant, sans comparer 
    essais += 1   # ici l'essai est valide, donc il compte
    if nombre < secret:  
        print("Trop petit !")
    elif nombre > secret:
        print("Trop grand !")
    else:
        gagner = True
        print("Gagné ! Bien joué !")
        break  # Gagné + break on sort de la boucle

if not gagner : # Gagné = False, on affiche le message de défaite avec le chiffre secret.
    print("Et c'est perdu, le nombre était : ", secret, "\n RETENTE !")

