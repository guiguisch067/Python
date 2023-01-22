#! python3


import csv
import sys


# Création du morpion vide

def creation_morpion():
    # data rows of csv file
    rows = [ ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'] ]
    # name of csv file
    morpion = "morpion.csv"
    # writing to csv file
    with open(morpion, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the data rows
        csvwriter.writerows(rows) 
    return morpion


def affiche_morpion(morpion):
    with open(morpion, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            print(', '.join(row))
    


def main():
    morpion = creation_morpion()
    print(f"On affiche la matrice vide : {affiche_morpion(morpion)}")
    affiche_morpion(morpion)
    # Ou version expert : affiche_morpion(creation_morpion())
    joueur = input("X ou O")
    with open(morpion, 'a') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|')
        csvwriter.writerow(joueur)
    print(f"On affiche la matrice avec joueur : {affiche_morpion(morpion)}")


main()