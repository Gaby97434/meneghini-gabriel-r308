import random
import unicodedata

# ---------- Fonctions de la partie A ----------

def ajouter_etudiant(d, nom, note):
    # Ajoute la clé au dictionnaire, ou met à jour sa valeur si elle existe déjà
    d[nom] = note

def sauvegarder(d, chemin):
    # Écrit le dictionnaire dans un fichier texte, une ligne "nom:note" par entrée
    with open(chemin, "w", encoding="utf-8") as f:
        for nom, note in d.items():
            f.write(f"{nom}:{note}\n")

def charger(chemin):
    # Lit un fichier "nom:note" et renvoie un dictionnaire (vide si le fichier est absent)
    d = {}
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for ligne in f:
                morceaux = ligne.strip().split(":")
                if len(morceaux) != 2:
                    continue
                nom = morceaux[0]
                try:
                    note = float(morceaux[1])
                except ValueError:
                    continue
                ajouter_etudiant(d, nom, note)
    except FileNotFoundError:
        pass
    return d

# ---------- Fonctions ----------

def choisir_mot(liste):
    # Renvoie un mot de la liste tiré au hasard, en majuscules
    mot = random.choice(liste)
    return mot.upper()

def masque(mot):
    # Renvoie une liste de "_" (une par lettre) ; les espaces restent des espaces
    return [" " if c == " " else "_" for c in mot]

def sans_accent(texte):
    # "É" devient "E" : on décompose la lettre (E + accent), puis on garde seulement les lettres de base
    decompose = unicodedata.normalize("NFD", texte)
    return "".join(c for c in decompose if unicodedata.category(c) != "Mn")

mots = ["Python", "réseau", "clavier", "transpiration", "bromance", "procrastination", "Éléphant", "équipe", "cage à puff"]

# ---------- Une partie de Pendu ----------

def jouer():
    # Joue une partie de Pendu, renvoie True si le joueur a gagné, False sinon
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

        if sans_accent(lettre) in deja_dites:
            print("La lettre a déjà été dite")
            continue
        deja_dites.append(sans_accent(lettre))   # on mémorise, sans accent

        if sans_accent(lettre) in sans_accent(mot):
            for i, l in enumerate(mot):
                if sans_accent(l) == sans_accent(lettre):
                    cache[i] = l
        else:
            erreurs += 1
            print("Non", lettre, "n'est pas dans ce mot là...")
            if erreurs == 6:
                print("C'est ta dernière chance !")

    if "_" not in cache:
        print("Gagné !", mot)
        return True
    else:
        print("Perdu, le mot était", mot)
        return False

# ---------- Programme principal ----------

scores = charger("scores.txt")
nom = input("Ton pseudo : ")
print("Bienvenue dans le jeu de pendu", nom,"t'es prêt ?" )

while True:
    if jouer():
        scores[nom] = scores.get(nom, 0.0) + 1
    print("Tes victoires :", scores.get(nom, 0))
    sauvegarder(scores, "scores.txt")
    if input("Rejouer ? (o/n) ").lower() != "o":
        break