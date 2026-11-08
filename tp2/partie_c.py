from partie_a import Grille
from partie_b import JoueurHumain, JoueurIA

def partie(joueur_x, joueur_o, afficher=True): # On définit la fonction partie
    grille = Grille()
    joueurs = [(joueur_x, "X"), (joueur_o, "O")] # On défini le signe des deux joueurs
    tour = 0
    while True:
        joueur, symbole = joueurs[tour % 2] #  On définit qui joue en premier et alterne à chaque tour 
        if afficher:
            grille.afficher()
        x, y = joueur.prochain_coup(grille, symbole)
        while not grille.jouer(x, y, symbole): # On teste si le coup joué est valide ou pas
            print("Coup invalide, rejoue")
            x, y = joueur.prochain_coup(grille, symbole) # Coup refusé : on redemande au même joueur
        if grille.est_gagnant(symbole): # On compare à la liste des combinaisons si la partie est gagnée ou non (la victoire est tester avant le nul, le dernier coup peux mener à une victoire)
            if afficher:
                grille.afficher()
            return symbole
        if grille.est_plein(): # On vérifie à la fin si le match est nul, toutes les cases sont remplies 
            if afficher:
                grille.afficher()
            return "nul"
        tour += 1

    
if __name__ == "__main__":
    for _ in range(20):
        print(partie(JoueurIA(), JoueurIA()))  
    print(partie(JoueurHumain(), JoueurIA()))