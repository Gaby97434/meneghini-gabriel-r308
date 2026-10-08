def ajouter_etudiant(d, nom, note):
    # Ajoute l'étudiant au dictionnaire, ou met à jour sa note s'il existe déjà
    d[nom] = note

def moyenne_classe(d):
    # Fait la moyenne des notes de tout les étudiants présents dans le dictionnaire, renvoie 0.0 s'il n'y a rien
    if not d:
        return 0.0
    return sum(d.values()) / len(d)

def meilleur_etudiant(d):
    # Renvoie l'étudiant avec la note la plus haute avec son nom, renvoie None si il n'y a rien 
    if not d:
        return None
    nom = max(d, key=d.get)
    return(nom, d[nom])

def sauvegarder(d, chemin):
    #Écrit le dictionnaire dans un fichier texte, une ligne "nom:note" par étudiant
    with open(chemin, "w", encoding="utf-8") as f:
        for nom, note in d.items():
            f.write(f"{nom}:{note}\n")

def charger(chemin):
    #Lit un fichier nom:note et renvoie un dictionnaire
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

notes = {}
ajouter_etudiant(notes, "Alice", 12.0)
ajouter_etudiant(notes, "Bob", 15.0)
ajouter_etudiant(notes, "Claire", 9.5)
print(notes)  # Affiche {'Alice': 12.0, 'Bob': 15.0, 'Claire': 9.5}
print(moyenne_classe(notes))  # Affiche 12.1666
print(meilleur_etudiant(notes))  # Affiche ('Bob', 15.0)

sauvegarder(notes, "notes.txt")
print(charger("notes.txt"))
print(charger("test.txt"))
print(charger("inexistant.txt"))