#! python3


# recherche des login et hostname dans une extraction depuis TEHTRIS
import csv
from ouvrir_un_csv import ouvrir_un_csv_vers_tableau_v2
from tableau2D_vers_Dico import create_dict_keys_2


def epuration_extraction_tehtris():

    # On transforme le fichier.csv extrait en tablau à 2 dimensions
    tableau = ouvrir_un_csv_vers_tableau_v2("TEHTRIS XDR - Endpoint - New filter.csv")
    # On transforme le tableau 2D en dictionnaire de liste permettant d'utiliser des clés 
    # Les clés correspondent aux colonnes d ela première ligne du tableau
    tabdico = create_dict_keys_2(tableau)

    for tab in tabdico:
        utilisateurs = tab['Username']
        PC = tab['UID']
        # Le champ UID est composé de 4 éléments séparés par des ; 
        # On ne sélectione que le 3e (donc idex 2 dans la liste)
        PC = PC.split(";")
        print(utilisateurs + ';' + PC[2])


def epuration_extraction_tehtris_dictReader():

    # coder la même fonction que dans epuration_extraction_tehtris
    # avec la librairie csv et la fonction dictReader()


# etape suivante, créer une classe

# etape suivant 2 : créer un nouveau fichier CSV

# fin


def main():
    epuration_extraction_tehtris()


if __name__ == "__main__":
    main()
