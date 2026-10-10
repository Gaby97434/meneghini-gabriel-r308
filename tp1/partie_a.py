# ----------  Partie A : gestion d'un dictionnaire d'étudiants, avec sauvegarde et chargement  -----------

def ajouter_etudiant(d, nom, note):
    # Ajoute l'étudiant au dictionnaire, ou met à jour sa note s'il est déjà enregistrer
    # Pas de return : la fonction reçoit le dictionnaire lui-même (pas une copie),
    # donc modifier d modifie aussi la variable de l'appelant
    d[nom] = note

def moyenne_classe(d):
    # Fait la moyenne des notes de tous les étudiants, renvoie 0.0 s'il n'y a personne 
    if not d:
        return 0.0  # une moyenne doit rester un nombre, on évite aussi la division par zéro
    return sum(d.values()) / len(d)

def meilleur_etudiant(d):
    # Renvoie le tuple (nom, note) du meilleur étudiant, ou None si le dictionnaire est vide
    if not d:
        return None  # S'il n'existe aucun meilleur étudiant : 0 serait une fausse note
    # key=d.get : on compare les noms selon leur note, pas par ordre alphabétique
    nom = max(d, key=d.get)
    return (nom, d[nom])

def sauvegarder(d, chemin):
    # Écrit le dictionnaire dans un fichier texte, une ligne "nom:note" par étudiant
    # Mode "w" : crée le fichier ou écrase son contenu s'il existe déjà
    with open(chemin, "w", encoding="utf-8") as f:
        for nom, note in d.items():
            f.write(f"{nom}:{note}\n")  # le ":" sépare le nom de la note, charger() recoupera la ligne dessus

def charger(chemin):
    # Lit un fichier "nom:note" et renvoie un dictionnaire (vide si le fichier est absent)
    d = {}
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for ligne in f:
                # strip() enlève le \n de fin, split(":") coupe en [nom, note]
                morceaux = ligne.strip().split(":")
                # Ligne mal formée (pas exactement 2 morceaux) : on la saute
                if len(morceaux) != 2:
                    continue  # Si le fichier texte a été modifié à la main et ne respecte plus le format il continue et la ligne est simplement ignorée
                nom = morceaux[0]
                try:
                    note = float(morceaux[1])
                except ValueError:
                    continue  # la note n'est pas un nombre : on saute la ligne
                ajouter_etudiant(d, nom, note)
    except FileNotFoundError:
        pass  # Si le fichier n'existe pas pass permet de ne pas planter et on renvoie le dictionnaire vide prêt à être rempli
    return d

# ---------- Tests ----------

notes = {}
ajouter_etudiant(notes, "Alice", 12.0)
ajouter_etudiant(notes, "Bob", 15.0)
ajouter_etudiant(notes, "Claire", 9.5)
print(notes)  # Affiche {'Alice': 12.0, 'Bob': 15.0, 'Claire': 9.5}
print(moyenne_classe(notes))  # Affiche 12.166666...(12.17 arrondi)
print(meilleur_etudiant(notes))  # Affiche ('Bob', 15.0)

sauvegarder(notes, "notes.txt")
print(charger("notes.txt"))
print(charger("test.txt"))
print(charger("inexistant.txt"))
