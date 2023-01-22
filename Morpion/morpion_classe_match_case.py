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
        print(self.case1, self.case2, self.case3, "\n") 
        print(self.case4, self.case5, self.case7, "\n") 
        print(self.case7, self.case8, self.case9, "\n") 


def choix_joueur():
    joueur = str(input("Quel est le joueur ?"))
    print(f"joueur : {joueur}")
    return joueur


def choix_case(joueur) -> str:
    test = False # On initilaise à False pour rentrer dans la boucle
    while not test:
        test = True # une fois dans la boucle, on remet à True - repasse à False si erreur dans le "else"
        case = int(input("Quelle est la case jouée ?"))
        print(f"case : {case}")
        match case:
            case 1:
                morpion.case1 = joueur
            case 2:
                morpion.case2 = joueur
            case 3:
                morpion.case3 = joueur
            case 4:
                morpion.case4 = joueur
            case 5:
                morpion.case5 = joueur
            case 6:
                morpion.case6 = joueur
            case 7:
                morpion.case7 = joueur
            case 8:
                morpion.case8 = joueur
            case 9:
                morpion.case9 = joueur
            case None:
                print("__ERREUR__ : Vous avez entré un chiffre incorrect")
                test = False # Entrée erronée, on réinitialise à False pour refaire un tour dans la boucle
    return case


def is_victoire():
    victoire = False
    #print("TODO")
    return victoire


if __name__ == "__main__":
    morpion = Morpion()
    while not is_victoire():
        joueur = choix_joueur()
        choix_case(joueur)
        morpion.afficher_Morpion()
