lignes = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
]

class Grille:
    def __init__(self):
        self.cases = [[" " for _ in range(3)] for _ in range(3)]

    def jouer(self, x, y, joueur):
        # Renvoie True si le coup est joué, False s'il est refusé
        if not (0<= x <= 2) or not (0 <= y <=2):
            print("Hors grille")
            return False
        if self.cases[x][y] != " ":
            print("Case occupée")
            return False
        self.cases[x][y] = joueur
        return True

    def afficher(self):
        # Affiche la grille : cases séparées par " | ", lignes séparées par "---------"
        for i, ligne in enumerate(self.cases):
            print(" | ".join(ligne))          
            if i < 2:
                print("---------")

    def est_gagnant(self, j):
        # True si le joueur j a aligné 3 symboles
        for ligne in lignes:
            if all(self.cases[x][y] == j for x, y in ligne): # Test pour voir si une dans le jeu un shéma ressemble à une combinaison gagnante 
                return True
        return False

    def est_plein(self):
        # True s'il n'y a plus aucune case libre
        for ligne in self.cases:
            for case in ligne:
                if case == " ": # Test pour voir si la case est encore libre ou pas 
                    return False     # une case libre : pas plein
        return True                  # on a tout vu, aucune libre


       

# ---------- Tests ----------
g = Grille()
print(g.jouer(0, 0, "X"))   # True
print(g.jouer(0, 0, "O"))   # False (occupée)
print(g.jouer(3, 0, "O"))   # False (hors grille)
print(g.jouer(-1, 0, "O"))  # False (hors grille)
print(g.cases)
g.jouer(0, 1, "O")
g.jouer(1, 1, "X")
g.afficher()
print(g.est_gagnant("X"))   # False
g.jouer(2, 2, "X")
print(g.est_gagnant("X"))   # True (diagonale)
print(g.est_plein())        # False
g2 = Grille()
g2.jouer(0, 2, "O")
g2.jouer(1, 1, "O")
g2.jouer(2, 0, "O")
print(g2.est_gagnant("O"))   # True (diagonale inverse)