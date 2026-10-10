import random
import unicodedata

# ---------- Fonctions de la partie A ----------

def ajouter_etudiant(d, nom, note):
    # Ajoute la clé au dictionnaire, ou met à jour sa valeur si elle existe déjà (voir partie A pour détails)
    d[nom] = note

def sauvegarder(d, chemin):
    # Écrit le dictionnaire dans un fichier texte, une ligne "nom:note" par entrée (voir partie A pour détails)
    with open(chemin, "w", encoding="utf-8") as f:
        for nom, note in d.items():
            f.write(f"{nom}:{note}\n")

def charger(chemin):
    # Lit un fichier "nom:note" et renvoie un dictionnaire (vide si le fichier est absent) (voir partie A pour détails)
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
    # Renvoie un mot de la liste tiré au hasard avec random.choice, en majuscules
    mot = random.choice(liste)
    return mot.upper()

def masque(mot):
    # Renvoie une liste de "_" (une par lettre) ; les espaces restent des espaces
    return [" " if c == " " else "_" for c in mot]

def sans_accent(texte):
    # "É" devient "E" (pour comparer E et É comme la même lettre)
    # NFD sépare la lettre de son accent : "É" devient "E" + "´" (2 caractères)
    decompose = unicodedata.normalize("NFD", texte)
    # "Mn" = catégorie des accents collés à une lettre : on les enlève, on garde le reste
    return "".join(c for c in decompose if unicodedata.category(c) != "Mn")

mots = ["Python", "réseau", "clavier", "transpiration", "bromance", "procrastination", "Éléphant", "équipe", "cage à puff"]

# ---------- Une partie de Pendu ----------

def jouer():
    # Joue une partie de Pendu, renvoie True si le joueur a gagné, False sinon
    mot = choisir_mot(mots)
    cache = masque(mot)
    erreurs = 0
    deja_dites = []

    while erreurs < 7 and "_" in cache:  # Tant que la variable erreurs est inférieure à 7 et qu'il reste des '_' on continue, sinon on arrête
        print(" ".join(cache), "| erreurs :", erreurs, "| déjà proposées :", deja_dites)
        lettre = input("Une lettre : ").upper()

        if len(lettre) != 1 or not lettre.isalpha():  # Refuse une saisie vide, de plusieurs caractères ou qui n’est pas une lettre (ne compte pas comme un essai) 
            print("Tape une seule lettre")
            continue

        if sans_accent(lettre) in deja_dites:  # Si le joueur tape 2 fois la même lettre il lui envoie un message (ne compte pas comme un essai)   
            print("La lettre a déjà été dite")
            continue
        deja_dites.append(sans_accent(lettre))   # On mémorise dans la variable deja_dites, sans accent

        if sans_accent(lettre) in sans_accent(mot):  # Si la lettre fait partie du mot on l'affiche à son bon emplacement 
            for i, l in enumerate(mot):  # Retrouve le bon emplacement avec enumerate
                if sans_accent(l) == sans_accent(lettre):
                    cache[i] = l
        else:
            erreurs += 1  # Si la lettre ne fait pas partie du mot on compte une erreur dans la variable erreur
            print("Non", lettre, "n'est pas dans ce mot là...")
            if erreurs == 6:  # Prévient le joueur qu'il est à son dernier essai
                print("C'est ta dernière chance !")

    if "_" not in cache:  # S'il n'y a plus de '_' le joueur gagne sinon il perd et on donne le mot qui était à deviner
        print("Gagné !", mot)
        return True  # Garde True pour une victoire pour l'enregistrement dans le Hall of Fame
    else:
        print("Perdu, le mot était", mot)
        return False

# ---------- Programme principal ----------

scores = charger("scores.txt")  # On utilise le fichier score.txt pour le Hall of Fame
nom = input("Ton pseudo : ").strip()  # Variable pour donner la clef des scores avec un pseudo personnalisable 
while nom == "" or ":" in nom:
    # strip() retire les espaces au début et à la fin : "Ana " et "Ana" restent le même joueur
    # Un pseudo fait seulement d'espaces devient "" et est refusé par la boucle
    nom = input("Pseudo invalide, change : ").strip()   
    
print("Bienvenue dans le jeu du pendu", nom,"t'es prêt ?" )

while True:  # Fonction de rejouer avec l'enregistrement du score en fonction des victoires
    if jouer():
        scores[nom] = scores.get(nom, 0.0) + 1
    print("Tes victoires :", scores.get(nom, 0.0))
    sauvegarder(scores, "scores.txt")
    if input("Rejouer ? (o/n) ").lower() != "o":
        break