from partie_a import Livre, Utilisateur
from partie_c import BibliothequePersistante

FICHIER = "livres.csv"

def menu():
    # Boucle principale : charge l'état au lancement, le sauvegarde en quittant
    b = BibliothequePersistante()
    b.charger(FICHIER)  # fichier absent : charger() ne plante pas, la bibliothèque reste vide

    while True:
        print("\n1 Ajouter un livre | 2 Ajouter un utilisateur | 3 Emprunter")
        print("4 Rendre | 5 Afficher les livres | 6 Quitter et sauvegarder")
        choix = input("Ton choix : ").strip()

        if choix == "1":
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()
            try:
                annee = int(input("Année : "))
            except ValueError:
                print("L'année doit être un nombre")
                continue  # on revient au menu sans ajouter le livre
            b.ajouter_livre(Livre(titre, auteur, annee))
            print("Livre ajouté")
        elif choix == "2":
            nom = input("Nom : ").strip()
            if nom == "":
                print("Le nom ne peut pas être vide")
            else:
                b.ajouter_utilisateur(Utilisateur(nom))
                print("Utilisateur ajouté")
        elif choix == "3":
            nom = input("Nom : ").strip()
            titre = input("Titre : ").strip()
            if b.emprunter(nom, titre):
                print("Emprunt réussi")
            else:
                print("Échec : nom ou titre inconnu, ou livre déjà emprunté")
        elif choix == "4":
            nom = input("Nom : ").strip()
            titre = input("Titre : ").strip()
            if b.rendre(nom, titre):
                print("Livre rendu")
            else:
                print("Échec : nom ou titre inconnu, ou ce n'est pas votre livre")
        elif choix == "5":
            b.afficher_livres()
        elif choix == "6":
            b.sauvegarder(FICHIER)  # on sauvegarde AVANT de sortir
            print("Sauvegardé, à bientôt")
            break  # sort de la boucle, donc du menu
        else:
            print("Choix invalide")

if __name__ == "__main__":
    menu()