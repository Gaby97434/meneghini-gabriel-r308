def ajouter_etudiant(d, nom, note):
    d[nom] = note

def moyenne_classe(d):
    if not d:
        return 0.0
    return sum(d.values()) / len(d)

def meilleur_etudiant(d):
    if not d:
        return None
    nom = max(d, key=d.get)
    return(nom, d[nom])

def sauvegarder(d, chemin):
    #Écrit le dictionnaire dans un fichier texte, une ligne "nom:note" par étudiant
    with open(chemin, "w", encoding="utf-8") as f:
        for nom, note in d.items():
            f.write(f"{nom}:{note}\n")

notes = {}
ajouter_etudiant(notes, "Alice", 12.0)
ajouter_etudiant(notes, "Bob", 15.0)
ajouter_etudiant(notes, "Claire", 9.5)
print(notes)  # Affiche {'Alice': 12.0, 'Bob': 15.0, 'Claire': 9.5}
print(moyenne_classe(notes))  # Affiche 12.1666
print(moyenne_classe({})) # 0.0
print(meilleur_etudiant(notes))  # Affiche 'Bob'
print(meilleur_etudiant({}))  # Affiche None
sauvegarder(notes, "notes.txt")