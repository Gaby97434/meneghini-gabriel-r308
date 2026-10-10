import random
import unicodedata 

def choisir_mot(liste):
    # Renvoie un mot de la liste tiré au hasard, en majuscules
    mot = random.choice(liste)
    return mot.upper()

def masque(mot):
    # Renvoie une liste de "_" de la même longueur que le mot
    return [" " if c == " " else "_" for c in mot]

def sans_accent(texte):
    # "É" devient "E" : on décompose la lettre (E + accent), puis on garde seulement les lettres de base 
    decompose = unicodedata.normalize("NFD", texte)
    return "".join(c for c in decompose if unicodedata.category(c) !="Mn")

mots = ["Python", "réseau", "clavier", "transpiration", "bromance", "procrastination", "Éléphant", "équipe", "intelligence artificielle", "cage à puff"]


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
    if sans_accent(lettre) in deja_dites:
        print("La lettre a déjà été dite")
        continue
    deja_dites.append(lettre)    # on mémorise la lettre

    if sans_accent(lettre) in sans_accent(mot):
            for i, l in enumerate(mot):
                if sans_accent(l) == sans_accent(lettre):
                    cache[i] = l # on révèle l (avec son accent), pas lettre                     # révéler toutes les positions (boucle enumerate)
    else:
        erreurs += 1
        print("Non", lettre,"n'est pas dans ce mot là...")
        if erreurs == 6:
            print("C'est ta dernière chance !")

if "_" not in cache:
    print("C'est gagné ! ", mot)
else:
    print("C'est perdu le mot était", mot)
# Après la boucle : victoire ou défaite ?
