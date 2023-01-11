#! python3

import csv

liste_headers = ["User","UID","IP"]
ligne1 = ["Jean","123","192.168.0.1"]
ligne2 = ["Michel","456","192.168.0.2"]
ligne3 = ["Jarre","789","192.168.0.3"]
tableau = [liste_headers]
print(tableau)
tableau.append(ligne1)
print(f"Tableau[1] = {tableau[1]}")
tableau.append(ligne2)
print(f"Tableau[2] = {tableau[2]}")
tableau.append(ligne3)
print(f"Tableau[3] = {tableau[3]}")

print(f"Tableau 1 et 1er élément : {tableau[1][0]}")

'''
with open("test_pypy.csv", 'w') as fichier:
    write_csv = csv.writer(fichier, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    write_csv.writerow(ligne1)
    write_csv.writerow(ligne2)
    write_csv.writerow(ligne3)


with open("test_pypy.csv", 'r') as fichier:
    reader_csv = csv.reader(fichier)
    for row in reader_csv:
        tableau.append(row)
'''


