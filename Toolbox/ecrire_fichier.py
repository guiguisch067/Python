#! python3

# écrire dans un fichier, basqiue


def ecrire_dans_fichier():
    fichier = open("test.txt", "a")
    fichier.writelines("\nBenoit")
    fichier.close()

ecrire_dans_fichier()