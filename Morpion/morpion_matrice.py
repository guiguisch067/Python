#! python3

morpion = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
joueur = ""
nbtour = 0


def afficher(): # une fonction bidon pour éviter d'utiliser cette horreur à chaque affichage
    print(f"{morpion[0]}\n{morpion[1]}\n{morpion[2]}\n")


# fonction principale pour positionner un pion X ou O à une position entre 1 et 9
def jeu(nbtour,joueur): 
    # On choisit le pion joué au premier tour uniquement
    test_pionOK = True
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
        test_numcase = int(input("Indiquer la case à jouer :\n1, 2, 3,\n4, 5, 6,\n7, 8, 9\n -->"))
        # On vérifie la position choisie
        if int(test_numcase) >= 1 and int(test_numcase) <= 9:
            # si l'entrée utilisateur est valide, on initialise les posiitons ligne et colonne
            ligne = (test_numcase - 1) // 3
            col = (test_numcase - 1) % 3
            if morpion[ligne][col] == "X" or morpion[ligne][col] == "O":
                print("__ERREUR__ : Cette case est déjà jouée, il faut en choisir une autre ! \n")
            else:
                numcase = test_numcase
                test_caseOK = False
        else:
            # Entrée erronée, on boucle jusqu'à que ce soit valide
            print("__ERREUR__ : Entrez un chiffre entre 1 et 9")
    print(f"\nVous avez choisit la case numéro : {numcase}\n")
    # On entre le pion du joueur à la valeur sélectionnée
    morpion[ligne][col] = joueur
    afficher()
    return joueur


def condition_victoire(joueur): # Fonction qui vérifie si une condition de victoireOK est remplie
    #lignes
    victoireOK = False
    for i in range(morpion):
        if morpion[i] == joueur:
            victoireOK = True
    
    #colonnes
    
    #diagonales
    
    
    return victoireOK


if __name__ == "__main__":
    joueur = jeu(nbtour,joueur)
    while (nbtour < 9): #and (condition_victoire() == False) : #tant que la victoire n'est pas déclarée on continue à jouer
        nbtour += 1
        joueur = jeu(nbtour,joueur)
        #if condition_victoire():
        #    print(f"_VICTOIRE_ du joueur : --- {joueur} ---")
    if nbtour >= 9:
        print("Nombre de tour terminé : __EGALITE__ !")