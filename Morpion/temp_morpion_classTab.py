#! python3


'''
class Morpion:
    def __init__(self) -> None:
        for i in range(9):
            self.case[i] = "-"
'''


class Morpion:
    def __init__(self) -> None:
            self.case = ["-" for i in range(9)]
      

    def afficher_Morpion(self) -> None: # une fonction bidon pour éviter d'utiliser cette horreur à chaque affichage
        for i in range(len(morpion.case)):
            print(self.case[i])
            if i % 3 == 3:
                print("\n") 


def choix_joueur() -> str:
    joueur = str(input("Quel est le joueur ?"))
    print(f"joueur : {joueur}")
    return joueur


def choix_case(joueur) -> None:
    test = False # On initilaise à False pour rentrer dans la boucle
    while not test:
        test = True # une fois dans la boucle, on remet à True - repasse à False si erreur dans le "else"
        case = int(input("Quelle est la case jouée ?"))
        # On contrôle l'entrée utilisateur
        if case in {1,2,3,4,5,6,7,8,9,10}:
            morpion.case[case-1] = joueur
        else:
            print("__ERREUR__ : Vous avez entré un chiffre incorrect")
            test = False # Entrée erronée, on réinitialise à False pour refaire un tour dans la boucle


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
