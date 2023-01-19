#! python3

morpion = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
joueur = ""
nbtour = 0


def afficher(): # une fonction bidon pour éviter d'utiliser cette horreur à chaque affichage
    print(morpion[0],morpion[1], morpion[2])
    print(morpion[3],morpion[4], morpion[5])
    print(morpion[6],morpion[7], morpion[8] + "\n")


#fonction permettant de choisir le 1er joueur puis de faire 1 sur 2
def choix_joueur(joueur: str):
    # On choisit le pion joué au premier tour uniquement
    print("TODO")
    

def choix_case():
    print("TODO")
    return joueur


# fonction principale pour positionner un pion X ou O à une position entre 1 et 9
def jeu(nbtour: int,joueur : str): 
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
        test_numcase = input("Indiquer la case à jouer :\n1, 2, 3,\n4, 5, 6,\n7, 8, 9\n -->")
        # On vérifie la position choisie dans la longueur de notre liste
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

'''
def condition_victoire(joueur: str) -> bool:
    is_victoire = False
    i = 0
    while i < len(morpion):
        # lignes
        if i in [0, 3, 6]:
            if morpion[i] == joueur and morpion[i+1] == joueur and morpion[i+2] == joueur:
                is_victoire = True
        # colonnes
        if i in [0, 1, 2]:
            if morpion[i] == joueur and morpion[i+3] == joueur and morpion[i+6] == joueur:
                is_victoire = True
        # diagonales
        if i == 0:
            if morpion[i] == joueur and morpion[i+4] == joueur and morpion[i+8] == joueur:
                is_victoire = True
        if i == 2:
            if morpion[i] == joueur and morpion[i+2] == joueur and morpion[i+4] == joueur:
                is_victoire = True
        i += 1
    return is_victoire
'''


def condition_victoire_match_case(joueur: str) -> bool:
    is_victoire = False
    match joueur:
        # ligne 1
        case morpion[0] and morpion[1] and morpion[2]:
            is_victoire = True
    return is_victoire



if __name__ == "__main__":
    joueur = jeu(nbtour,joueur)
    while nbtour < 9 and condition_victoire(joueur) == False : #tant que la victoire n'est pas déclarée on continue à jouer
        nbtour += 1
        joueur = jeu(nbtour,joueur)
        if condition_victoire(joueur):
            print(f"_VICTOIRE_ du joueur : --- {joueur} ---")
    if nbtour >= 9:
        print("Nombre de tour terminé : __EGALITE__ !")
