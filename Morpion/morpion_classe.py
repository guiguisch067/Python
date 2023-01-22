#! python3

import sys

'''
class Morpion:
    def __init__(self) -> None:
        for i in range(9):
            self.case[i] = "-"
'''


class TicTacToe:
    def __init__(self):
        self.case1 = "-"
        self.case2 = "-"
        self.case3 = "-"
        self.case4 = "-"
        self.case5 = "-"
        self.case6 = "-"
        self.case7 = "-"
        self.case8 = "-"
        self.case9 = "-"
      

    def afficher_Morpion(self) -> None: # une fonction bidon pour éviter d'utiliser cette horreur à chaque affichage
        print(f"{self.case1} {self.case2} {self.case3} \n") 
        print(f"{self.case4} {self.case5} {self.case6} \n") 
        print(f"{self.case7} {self.case8} {self.case9} \n") 


class Player:
    def __init__(self):
        self.pion = "X" 
        #TODO utiliser un input avec contrôle de l'entrée utilisateur


    def switch_joueur(self):
        if self.pion == "X":
            self.pion = "O"
        else:
            self.pion = "X"
        print(f"C'est au tour du joueur : {self.pion}")


def choix_case(morpion:TicTacToe, joueur: Player) -> str:
    case = int(input("Quelle est la case jouée ?"))
    print(f"case : {case}")
    if case == 1:
        morpion.case1 = joueur.pion
    elif case == 2:
        morpion.case2 = joueur.pion
    elif case == 3:
        morpion.case3 = joueur.pion
    elif case == 4:
        morpion.case4 = joueur.pion
    elif case == 5:
        morpion.case5 = joueur.pion
    elif case == 6:
        morpion.case6 = joueur.pion
    elif case == 7:
        morpion.case7 = joueur.pion
    elif case == 8:
        morpion.case8 = joueur.pion
    elif case == 9:
        morpion.case9 = joueur.pion
    else:
        print("__ERREUR__ : Vous avez entré un chiffre incorrect")
        sys.exit()


def is_victoire(morpion: TicTacToe, joueur: Player) -> bool:
    victoire = False
    #lignes
    if (morpion.case1 and morpion.case2 and morpion.case3) == joueur.pion:
        victoire = True
    if (morpion.case4 and morpion.case5 and morpion.case6) == joueur.pion:
        victoire = True
    if (morpion.case7 and morpion.case8 and morpion.case9) == joueur.pion:
        victoire = True
    #colonnes
    if (morpion.case1 and morpion.case4 and morpion.case7) == joueur.pion:
        victoire = True
    if (morpion.case2 and morpion.case5 and morpion.case8) == joueur.pion:
        victoire = True
    if (morpion.case3 and morpion.case6 and morpion.case9) == joueur.pion:
        victoire = True
    #diagonales
    if (morpion.case1 and morpion.case5 and morpion.case9) == joueur.pion:
        victoire = True
    if (morpion.case3 and morpion.case5 and morpion.case7) == joueur.pion:
        victoire = True
    return victoire


if __name__ == "__main__":
    morpion = TicTacToe()
    joueur = Player()
    while True:
        choix_case(morpion, joueur)
        morpion.afficher_Morpion()
        if is_victoire(morpion, joueur):
            print(f"__Victoire de : {joueur.pion} __")
            sys.exit()
        else:
            joueur.switch_joueur()
