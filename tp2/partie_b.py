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
                print(" Utilise des nombres pour te placer c'est plus clair ")

class JoueurIA: # Un joueur IA qui va jouer un coup au hasard parmis les cases libre dans la grille
    def prochain_coup(self, tab, symbole):
        # Renvoie une case libre au hasard
        libres = [] # On crée une liste qui va répertorier toutes les cases vides
        for x in range(3):
            for y in range(3): 
                if tab.cases[x][y] == " ": # Condition pour savoir si la case est vide 
                    libres.append((x, y))
        return random.choice(libres) # L'IA joue une case aléatoire dans cette liste

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