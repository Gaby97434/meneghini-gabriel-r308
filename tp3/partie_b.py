from partie_a import Livre, Utilisateur

class Bibliotheque:
    def __init__(self):
        self.livres = {}          # titre -> Livre
        self.utilisateurs = {}    # nom -> Utilisateur

    def ajouter_livre(self, livre):
        self.livres[livre.titre] = livre                       # self.livres[livre.titre] = livre

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs[utilisateur.nom] = utilisateur                       

    def emprunter(self, nom, titre):
        # True si l'emprunt réussit, False sinon (nom/titre inconnu, déjà emprunté)
        if nom not in self.utilisateurs:                   # nom inconnu
            return False
        if titre not in self.livres:                   # titre inconnu
            return False                
        utilisateur = self.utilisateurs[nom]          #  déléguer à l'utilisateur
        livre = self.livres[titre]
        return utilisateur.emprunter_livre(livre)

    def rendre(self, nom, titre):
        # Rend un livre ; False si nom/titre inconnu ou si ce n'est pas son livre
        if nom not in self.utilisateurs:
            return False
        if titre not in self.livres:
            return False
        return self.utilisateurs[nom].rendre_livre(self.livres[titre])                    

    def afficher_livres(self):
    # Affiche les livres disponibles, puis les livres empruntés
        print("Disponibles :")
        for livre in self.livres.values():
            if livre.disponible:
                livre.afficher()
        print("Empruntés :")
        for livre in self.livres.values():
            if not livre.disponible:
                livre.afficher()                       


if __name__ == "__main__":

    b = Bibliotheque()
    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.ajouter_utilisateur(Utilisateur("Léo"))

    print(b.emprunter("Ana", "1984"))    # True
    print(b.emprunter("Léo", "1984"))    # False : déjà emprunté
    print(b.emprunter("Zoé", "1984"))    # False : nom inconnu
    print(b.emprunter("Ana", "Dune"))    # False : titre inconnu
    b.afficher_livres()
    print(b.rendre("Léo", "1984"))       # False : ce n'est pas son livre
    print(b.rendre("Ana", "1984"))       # True