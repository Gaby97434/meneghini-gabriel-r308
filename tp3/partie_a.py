class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True
        self.emprunteur = None        # personne ne l'a au départ

    def afficher(self):
        # Affiche titre, auteur, année et l'état (disponible ou emprunté par ...)
        if self.disponible:
            etat = "disponible"
        else:
            etat = f"emprunté par {self.emprunteur}"
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")                          

    def emprunter(self, nom):
        # True si l'emprunt réussit, False si le livre est déjà pris
        if not self.disponible:    # déjà emprunté
            return False
        self.disponible = False    # marquer indisponible + mémoriser nom
        self.emprunteur = nom
        return True

    def rendre(self):
        # True si le livre était emprunté, False sinon
        if self.disponible:        # déjà là : rien à rendre
            return False
        self.disponible = True     # de nouveau disponible
        self.emprunteur = None     # personne ne l'a plus
        return True


class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []           

    def emprunter_livre(self, livre):
        # Emprunte via le livre ; si ça marche, l'ajoute à la liste
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)       # ajoute le livre à la liste
            return True
        return False

    def rendre_livre(self, livre):
        # Rend un livre que cet utilisateur a emprunté ; False sinon
        if livre not in self.emprunts:   # vérifie si le livre n'est pas dans la liste des emprunts
            return False
        livre.rendre()
        self.emprunts.remove(livre)   # on le retire ensuite de la liste
        return True                           

    def afficher_emprunts(self):
        # Affiche les livres empruntés par cet utilisateur
        if not self.emprunts:
            print(f"{self.nom} n'a aucun emprunt")  # si la personne n'a rien pris on affiche qu'il n'a aucun emprunt  
            return
        for livre in self.emprunts:
            livre.afficher()  # Sinon on affiche les livres pris                     



if __name__ == "__main__":
    l = Livre("1984", "Orwell", 1949)
    print(l.emprunter("Ana"))   # True
    print(l.emprunter("Léo"))   # False
    print(l.rendre())           # True
    l.afficher()

    ana = Utilisateur("Ana")
    print(ana.emprunter_livre(l))   # True
    print(ana.emprunter_livre(l))   # False (déjà pris, pas de doublon)
    ana.afficher_emprunts()
    print(ana.rendre_livre(l))      # True
    print(len(ana.emprunts))        # 0

    leo = Utilisateur("Léo")
    ana.emprunter_livre(l)
    print(leo.rendre_livre(l))   # False : ce n'est pas son livre
    print(ana.rendre_livre(l))   # True