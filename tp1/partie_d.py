import random

def choisir_mot(liste):
    # Renvoie un mot de la liste tiré au hasard, en majuscules
    mot = random.choice(liste)
    return mot.upper()

def masque(mot):
    # Renvoie une liste de "_" de la même longueur que le mot
    return ["_"] * len(mot)

mots = ["python", "reseau", "clavier", "transpiration", "bromance", "procrastination"]

mot = choisir_mot(mots)
cache = masque(mot)
erreurs = 0
deja_dites = []

while erreurs < 7 and "_" in cache:
    print(" ".join(cache), "| erreurs :", erreurs, "| déjà proposées :", deja_dites)
    lettre = input("Une lettre : ").upper()

    if len(lettre) != 1 or not lettre.isalpha():
        print("Tape une seule lettre")
        continue
    if lettre in deja_dites:
        print("La lettre a déjà été dite")                      # message "déjà dit", et on ne compte rien
        continue
    deja_dites.append(lettre)    # on mémorise la lettre

    if lettre in mot:
        for i, l in enumerate(mot):
            if l == lettre:
                cache[i] = l                     # révéler toutes les positions (boucle enumerate)
    else:
        erreurs += 1
        print("Non", lettre,"n'est pas dans ce mot là...")
        if erreurs == 6:
            print("C'est ta dernière chance !")

if "_" not in cache:
    print("C'est gagné ! ")
else:
    print("C'est perdu le mot était", mot)
# Après la boucle : victoire ou défaite ?

print(mot)