import csv
from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque

class BibliothequePersistante(Bibliotheque):
    # Une Bibliotheque qui sait se sauvegarder et se recharger en CSV
    # (hérite de tout ce que fait Bibliotheque, on ajoute juste deux méthodes)

    def sauvegarder(self, chemin):
        # Un livre par ligne : titre, auteur, année, disponible, emprunteur
        with open(chemin, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for livre in self.livres.values():
                # emprunteur None -> "" (un fichier ne stocke que du texte)
                writer.writerow([livre.titre, livre.auteur, livre.annee,
                                 livre.disponible, livre.emprunteur or ""])

    def charger(self, chemin):
        # Recharge les livres ; fichier absent ou ligne abîmée : on ignore
        try:
            with open(chemin, "r", newline="", encoding="utf-8") as f:
                for ligne in csv.reader(f):
                    if len(ligne) != 5:
                        continue
                    try:
                        livre = Livre(ligne[0], ligne[1], int(ligne[2]))
                    except ValueError:
                        continue
                    livre.disponible = (ligne[3] == "True")  # bool("False") serait True !
                    nom = ligne[4] or None                   # "" redevient None
                    livre.emprunteur = nom
                    if nom is not None:
                        if nom not in self.utilisateurs:
                            self.ajouter_utilisateur(Utilisateur(nom))
                        # sans ça, l'utilisateur ne pourrait pas rendre le livre
                        self.utilisateurs[nom].emprunts.append(livre)
                    self.ajouter_livre(livre)
        except FileNotFoundError:
            pass  # fichier absent au lancement : bibliothèque vide

if __name__ == "__main__":
    b = BibliothequePersistante()
    b.ajouter_livre(Livre("Le Petit Prince, tome 1", "Saint-Exupéry", 1943))
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.ajouter_utilisateur(Utilisateur("Léo"))
    b.emprunter("Ana", "1984")
    b.sauvegarder("livres.csv")

    b2 = BibliothequePersistante()
    b2.charger("livres.csv")
    b2.afficher_livres()
    print(b2.rendre("Léo", "1984"))   # False
    print(b2.rendre("Ana", "1984"))   # True