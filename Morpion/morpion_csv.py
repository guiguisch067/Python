#! python3


import csv
import sys


# Création du morpion vide

# data rows of csv file
rows: list[list] = [ ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-'] ]
# name of csv file
morpion: str = "morpion.csv"
# boule
i: int = 0
# writing to csv file
with open(morpion, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile, delimiter=',', lineterminator='\n', )
    # writing the data rows
    csvwriter.writerows(rows)
    while i in range(2): #devrait etre 9, tests temporaires
        print("Quel est le joueur ? X ou O ")
        joueur = str(input())
        print("quelle est la position à jouer ? col : ")
        col = int(input())
        print("quelle est la position à jouer ? line : ")
        line = int(input())
        rows[line][col] = joueur
        csvwriter.writerow(rows)
        i += 1


def affiche_morpion(morpion: str):
    with open(morpion, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', lineterminator='\n')
        for row in reader:
            print(', '.join(row))


affiche_morpion(morpion)