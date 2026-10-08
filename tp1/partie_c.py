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
print(mot)
print(masque(mot))
print(masque("PYTHON")) 