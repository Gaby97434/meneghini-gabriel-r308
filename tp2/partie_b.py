import random
from partie_a import Grille   # sert au test en bas ; les joueurs reçoivent la grille en paramètre

class JoueurHumain: # Un joueur humain qui va saisir la position au clavier
    def prochain_coup(self, tab, symbole):
        # Demande ligne et colonne au clavier, renvoie (x, y)
        while True:
            try:
                x = int(input("Ligne (0-2) : "))
                y = int(input("Colonne (0-2) : "))
                return x, y
            except ValueError:
                print("Utilise des nombres pour te placer c'est plus clair")

class JoueurIA: # Un joueur IA qui va jouer un coup au hasard parmi les cases libres dans la grille
    def prochain_coup(self, tab, symbole):
        # Renvoie une case libre au hasard
        libres = [] # On crée une liste qui va répertorier toutes les cases vides
        for x in range(3):
            for y in range(3): 
                if tab.cases[x][y] == " ": # Condition pour savoir si la case est vide 
                    libres.append((x, y))
        return random.choice(libres) # L'IA joue une case aléatoire dans cette liste


class JoueurIAMalin: # IA qui gagne si possible, sinon bloque, sinon joue au hasard
    def coup_gagnant(self, tab, symbole):
        # Renvoie une case (x, y) qui fait gagner 'symbole', sinon None
        for x in range(3):
            for y in range(3):
                if tab.cases[x][y] == " ":           # Condition pour savoir si la case est vide 
                    tab.cases[x][y] = symbole        # 1. on pose
                    gagne = tab.est_gagnant(symbole) # 2. on teste
                    tab.cases[x][y] = " "            # poser, tester, effacer (3 lignes)
                    if gagne:
                        return (x, y)
        return None              # aucune case gagnante

    def prochain_coup(self, tab, symbole):
        # 1. gagner  2. bloquer  3. hasard
        if symbole == "X":
            adversaire = "O"
        else:
            adversaire = "X"

        coup = self.coup_gagnant(tab, symbole) # Règle 1 : mon coup gagnant
        if coup is not None:
            return coup

        coup = self.coup_gagnant(tab, adversaire) # Règle 2 (coup gagnant de l'adversaire)
        if coup is not None:                                      
            return coup

        return JoueurIA().prochain_coup(tab, symbole)   # On réutilise JoueurIA

if __name__ == "__main__":
    # ---------- Tests ----------
    ia = JoueurIA()
    g3 = Grille()
    print(ia.prochain_coup(g3, "O"))   # un (x, y) libre

    g4 = Grille()
    for x in range(3):
        for y in range(3):
            if (x, y) != (1, 2):
                g4.jouer(x, y, "X")
    for _ in range(5):
        print(ia.prochain_coup(g4, "O"))   # toujours (1, 2)

    g5 = Grille()
    g5.jouer(0, 0, "X"); g5.jouer(0, 1, "X"); g5.jouer(1, 1, "O")
    ia = JoueurIAMalin()
    print(ia.coup_gagnant(g5, "X"))   # (0, 2) : X peut gagner ici
    print(ia.coup_gagnant(g5, "O"))   # None   : O n'a pas de coup gagnant
    g5.afficher()                     # la grille ne doit pas avoir changé
    g6 = Grille()                                   # X X _ / _ O _ / _ _ _
    g6.jouer(0, 0, "X"); g6.jouer(0, 1, "X"); g6.jouer(1, 1, "O")
    print(JoueurIAMalin().prochain_coup(g6, "O"))   # (0, 2) : bloque

    g2 = Grille()                                  # O O _ / X X _ / _ _ _
    g2.jouer(0, 0, "O"); g2.jouer(0, 1, "O")
    g2.jouer(1, 0, "X"); g2.jouer(1, 1, "X")
    print(JoueurIAMalin().prochain_coup(g2, "O"))  # (0, 2) : gagne