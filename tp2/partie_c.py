from partie_a import Grille
from partie_b import JoueurHumain, JoueurIA, JoueurIAMalin

# ---------- Scores (fichier texte) ----------

def charger_scores(chemin):
    # Renvoie un dictionnaire nom -> [victoires, nuls, défaites]
    scores = {}
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for ligne in f:
                morceaux = ligne.strip().split(":")
                if len(morceaux) != 4:  # ligne mal formée : on la saute
                    continue
                try:
                    v, n, d = int(morceaux[1]), int(morceaux[2]), int(morceaux[3])
                except ValueError:  # un des scores n'est pas un nombre : on saute
                    continue
                scores[morceaux[0]] = [v, n, d]
    except FileNotFoundError:
        pass  # fichier absent : on part avec un dictionnaire vide
    return scores

def sauvegarder_scores(scores, chemin):
    # Écrit une ligne "nom:victoires:nuls:défaites" par joueur
    with open(chemin, "w", encoding="utf-8") as f:
        for nom, (v, n, d) in scores.items():
            f.write(f"{nom}:{v}:{n}:{d}\n")

def enregistrer(scores, nom_x, nom_o, resultat):
    # Met à jour les scores ; resultat vaut "X", "O" ou "nul"
    for nom in (nom_x, nom_o):
        scores.setdefault(nom, [0, 0, 0])  # crée la ligne si le joueur est nouveau
    if resultat == "nul":
        scores[nom_x][1] += 1
        scores[nom_o][1] += 1
    elif resultat == "X":
        scores[nom_x][0] += 1  # victoire de X
        scores[nom_o][2] += 1  # défaite de O
    else:
        scores[nom_o][0] += 1  # victoire de O
        scores[nom_x][2] += 1  # défaite de X

def afficher_scores(scores, noms):
    # Affiche victoires / nuls / défaites et le taux de victoires de chaque joueur
    for nom in noms:
        v, n, d = scores[nom]
        total = v + n + d
        taux = v / total * 100 if total > 0 else 0.0  # évite la division par zéro
        print(f"{nom} : {v} V / {n} N / {d} D ({taux:.0f}% de victoires)")

def demander_pseudo(message):
    # Redemande tant que le pseudo est vide, contient ":" (il casserait le fichier) ou vaut "IA"
    while True:
        nom = input(message).strip()
        if nom != "" and ":" not in nom and nom != "IA":
            return nom
        print("Pseudo invalide")

# ---------- Une partie ----------

def partie(joueur_x, joueur_o, afficher=True):
    # Joue une partie complète, renvoie "X", "O" ou "nul"
    grille = Grille()
    joueurs = [(joueur_x, "X"), (joueur_o, "O")]
    tour = 0
    while True:
        joueur, symbole = joueurs[tour % 2]  # tour % 2 alterne : 0, 1, 0, 1...
        if afficher:
            grille.afficher()
        x, y = joueur.prochain_coup(grille, symbole)
        while not grille.jouer(x, y, symbole):  # coup refusé : on redemande au même joueur
            print("Coup invalide, rejoue")
            x, y = joueur.prochain_coup(grille, symbole)
        if grille.est_gagnant(symbole):  # victoire testée avant le nul : le dernier coup peut gagner
            if afficher:
                grille.afficher()
            return symbole
        if grille.est_plein():  # plus de case libre et personne n'a gagné
            if afficher:
                grille.afficher()
            return "nul"
        tour += 1  # on change de joueur seulement à la fin

# ---------- Menu ----------

def menu():
    # Choix 1 ou 2 joueurs, puis parties à la suite avec scores sauvegardés
    scores = charger_scores("scores_morpion.txt")

    mode = input("1 ou 2 joueurs ? ")
    while mode not in ("1", "2"):
        mode = input("Tape 1 ou 2 : ")

    nom_x = demander_pseudo("Pseudo joueur X : ")
    if mode == "1":
        nom_o, joueur_o = "IA", JoueurIA()
    else:
        nom_o = demander_pseudo("Pseudo joueur O : ")
        while nom_o == nom_x:  # deux pseudos identiques mélangeraient les scores
            print("Choisis un pseudo différent")
            nom_o = demander_pseudo("Pseudo joueur O : ")
        joueur_o = JoueurHumain()

    while True:
        resultat = partie(JoueurHumain(), joueur_o)
        enregistrer(scores, nom_x, nom_o, resultat)
        sauvegarder_scores(scores, "scores_morpion.txt")
        afficher_scores(scores, (nom_x, nom_o))
        if input("Rejouer ? (o/n) ").lower() != "o":
            break

# ---------- Tests ----------

def tests():
    # IA contre IA : chaque partie doit finir par X, O ou nul, sans plantage
    for _ in range(20):
        print(partie(JoueurIA(), JoueurIA(), afficher=False))
    resultats = [partie(JoueurIAMalin(), JoueurIA(), afficher=False) for _ in range(20)]
    print(resultats.count("X"), "victoires malin,", resultats.count("O"), "défaites,", resultats.count("nul"), "nuls")

if __name__ == "__main__":
    menu()
    # tests()   # décommente pour lancer les tests IA contre IA