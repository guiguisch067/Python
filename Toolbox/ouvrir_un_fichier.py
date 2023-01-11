#! python3

def temp_open_classique(fichier):
    fichier = open(fichier, "r")
    for ligne in fichier.readlines():
        print(ligne)
    fichier.close()