#! python3


'''
class Morpion:
    def __init__(self) -> None:
        for i in range(9):
            self.case[i] = "-"
'''


class Morpion:
    def __init__(self) -> None:
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


class Joueur:
    def __init__(self) -> None:
        self.joueur = str(input("Quel est le joueur ?"))
        

    def switch_joueur(self) -> str:
        if joueur == "X":
            self.joueur = "O"
        else:
            self.joueur = "X"
        print(f"joueur : {self.joueur}")
        return self.joueur


def choix_case(joueur) -> str:
    test = False # On initilaise à False pour rentrer dans la boucle
    while not test:
        test = True # une fois dans la boucle, on remet à True - repasse à False si erreur dans le "else"
        case = int(input("Quelle est la case jouée ?"))
        print(f"case : {case}")
        if case == 1:
            morpion.case1 = joueur
        elif case == 2:
            morpion.case2 = joueur
        elif case == 3:
            morpion.case3 = joueur
        elif case == 4:
            morpion.case4 = joueur
        elif case == 5:
            morpion.case5 = joueur
        elif case == 6:
            morpion.case6 = joueur
        elif case == 7:
            morpion.case7 = joueur
        elif case == 8:
            morpion.case8 = joueur
        elif case == 9:
            morpion.case9 = joueur
        else:
            print("__ERREUR__ : Vous avez entré un chiffre incorrect")
            test = False # Entrée erronée, on réinitialise à False pour refaire un tour dans la boucle
    return case


def is_victoire(joueur) -> bool:
    victoire = False
    #lignes
    if (morpion.case1 and morpion.case2 and morpion.case3) == joueur:
        victoire = True
    elif (morpion.case4 and morpion.case5 and morpion.case6) == joueur:
        victoire = True
    elif (morpion.case7 and morpion.case8 and morpion.case9) == joueur:
        victoire = True
    #colonnes
    elif (morpion.case1 and morpion.case4 and morpion.case7) == joueur:
        victoire = True
    elif (morpion.case2 and morpion.case5 and morpion.case8) == joueur:
        victoire = True
    elif (morpion.case3 and morpion.case6 and morpion.case9) == joueur:
        victoire = True
    #diagonales
    elif (morpion.case1 and morpion.case5 and morpion.case5) == joueur:
        victoire = True
    elif (morpion.case3 and morpion.case5 and morpion.case7) == joueur:
        victoire = True
    else:
        return victoire


if __name__ == "__main__":
    morpion = Morpion()
    joueur = Joueur()
    while not is_victoire(joueur):
        choix_case(joueur)
        morpion.afficher_Morpion()
        joueur = Joueur.switch_joueur(joueur)
    if is_victoire(joueur):
        print(f"__Victoire de : {joueur} __")
    else:
        print(f"__EGALITE, fin de la partie__")
