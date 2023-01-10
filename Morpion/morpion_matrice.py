#! python3

morpion = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
joueur = ""
nbtour = 0
test = "test"


def afficher(): # une fonction bidon pour éviter d'utiliser cette horreur à chaque affichage
    print(morpion[0],morpion[1], morpion[2])
    print(morpion[3],morpion[4], morpion[5])
    print(morpion[6],morpion[7], morpion[8] + "\n")


# fonction principale pour positionner un pion X ou O à une position entre 1 et 9
def jeu(nbtour,joueur): 
    # On choisit le pion joué au premier tour uniquement
    test_pionOK= True
    if nbtour == 0:
        while test_pionOK: # On vérifie le pion joué
            # variable temporaire pour vérifier l'entrée
            test_pionjoueur = input("\nIndiquer le pion du joueur : X ou O\n-->")
            if str(test_pionjoueur) == ("X") or str(test_pionjoueur) == ("O"):
                joueur = test_pionjoueur
                test_pionOK = False
            else: # Entrée erronée, on boucle jusqu'à que ce soit valide
                print("__ERREUR__ : Veuillez entrer un pion X ou O")                
    # on switch automatiquement le joueur une fois sur 2 après le 1er tour
    elif joueur == "X": 
        joueur = "O"
    else:
        joueur = "X"
    print(f"C'est au tour du joueur {joueur}\n")
    # Maintenant on choisit la case à jouer
    test_caseOK = True # booléen pour contrôler la boucle
    while test_caseOK:
        # variable temporaire pour vérifier l'entrée
        test_numcase = input("Indiquer la case à jouer :\n1, 2, 3,\n4, 5, 6,\n7, 8, 9\n -->")
        # On vérifie la position choisie
        if int(test_numcase) >= 1 and int(test_numcase) <=9:
            if morpion[int(test_numcase)-1] == "X" or morpion[int(test_numcase)-1] == "O":
                print("__ERREUR__ : Cette case est déjà jouée, il faut en choisir une autre ! \n")
            else:
                numcase = test_numcase
                test_caseOK = False
        else:
            # Entrée erronée, on boucle jusqu'à que ce soit valide
            print("__ERREUR__ : Entrez un chiffre entre 1 et 9")
    print(f"\nVous avez choisit la case numéro : {numcase}\n")
    morpion[int(numcase)-1] = joueur # conversion dégueulasse pour ne pas commencer à 0 du pdv joueur
    afficher()
    return joueur


def condition_victoire(): # Fonction qui vérifie si une condition de victoireOK est remplie
    #lignes
    victoireOK = False
    if morpion[0] == "X" and morpion[1] == "X" and morpion[2] == "X":
        print("victoire ligne 1")
        victoireOK = True
    if morpion[3] == "X" and morpion[4] == "X" and morpion[5] == "X":
        print("victoire ligne 2")
        victoireOK = True
    if morpion[6] == "X" and morpion[7] == "X" and morpion[8] == "X":
        print("victoire ligne 3")
        victoireOK = True
    if morpion[0] == "O" and morpion[1] == "O" and morpion[2] == "O":
        print("victoire ligne 1")
        victoireOK = True
    if morpion[3] == "O" and morpion[4] == "O" and morpion[5] == "O":
        print("victoire ligne 2")
        victoireOK = True
    if morpion[6] == "O" and morpion[7] == "O" and morpion[8] == "O":
        print("victoire ligne 3")
        victoireOK = True
    #colonnes
    if morpion[0] == "X" and morpion[3] == "X" and morpion[6] == "X":
        print("victoire colonne 1")
        victoireOK = True
    if morpion[1] == "X" and morpion[4] == "X" and morpion[7] == "X":
        print("victoire colonne 2")
        victoireOK = True
    if morpion[2] == "X" and morpion[5] == "X" and morpion[8] == "X":
        print("victoire colonne 3")
        victoireOK = True
    if morpion[0] == "O" and morpion[3] == "O" and morpion[6] == "O":
        print("victoire colonne 1")
        victoireOK = True
    if morpion[1] == "O" and morpion[4] == "O" and morpion[7] == "O":
        print("victoire colonne 2")
        victoireOK = True
    if morpion[2] == "O" and morpion[5] == "O" and morpion[8] == "O":
        print("victoire colonne 3")
        victoireOK = True
    #diagonales
    if morpion[0] == "X" and morpion[4] == "X" and morpion[8] == "X":
        print("victoire diagonale 1")
        victoireOK = True
    if morpion[2] == "X" and morpion[4] == "X" and morpion[7] == "X":
        print("victoire diagonale 2")
        victoireOK = True
    if morpion[0] == "O" and morpion[4] == "O" and morpion[8] == "O":
        print("victoire diagonale 1")
        victoireOK = True
    if morpion[2] == "O" and morpion[4] == "O" and morpion[7] == "O":
        print("victoire diagonale 2")
        victoireOK = True
    
    return victoireOK


if __name__ == "__main__":
    joueur = jeu(nbtour,joueur)
    while (nbtour < 9) and (condition_victoire() == False) : #tant que la victoire n'est pas déclarée on continue à jouer
        nbtour += 1
        joueur = jeu(nbtour,joueur)
        if condition_victoire():
            print(f"_VICTOIRE_ du joueur : --- {joueur} ---")
    if nbtour >= 9:
        print("Nombre de tour terminé : __EGALITE__ !")