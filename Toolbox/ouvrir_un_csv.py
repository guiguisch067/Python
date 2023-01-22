#! python3
# manipulations de fichiers csv

# import logging

import csv


def ouvrir_un_csv_vers_dico_v1(fichier):
    # On ouvre un fichier CSV qui contient à minima 2 colonnes dont les titres sont "Plugin" et "Plugin Name"
    with open(fichier, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        line_count = 0
        for row in csvreader:
            if line_count == 0:
                spool = 'Column names are' + ", ".join(row)
                line_count += 1
            spool += "\n Numéro du plugin utilisé : " + row["Plugin"] + "nom du plugin : " + row["Plugin Name"]
            line_count += 1
    return spool



def ouvrir_un_csv_vers_dico_v2(fichier):
    with open(fichier, newline='') as csvfile:
        # create a CSV reader object
        csvreader = csv.DictReader(csvfile)
        # create an empty list to store the dictionaries
        dict_list = []
        # iterate over the rows in the reader
        for ligne in csvreader:
            # append each row to the list as a dictionary
            dict_list.append(dict(ligne))

    return dict_list
    # example usage
    # dict_list = csv_to_dict('myfile.csv')
    # print(dict_list)


def ouvrir_un_csv_vers_tableau_v1(fichier):

    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(fichier, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    # printing first 5 rows
    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        # parsing each column of a row
        for col in row:
            print("%10s" % col, end=" "),
        print('\n')


def ouvrir_un_csv_vers_tableau_v2(fichiercsv):
    # reading csv file
    with open(fichiercsv, 'r', newline='') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile, delimiter=';')
        # initializing the titles and rows list
        tableau = []
        # la variable ligne sera une liste de tous les éléments d'une ligne du fichier .csv
        for ligne in csvreader:
            tableau.append(ligne)
    # On peut donc sélectionner une ligne complète avec tableau[i] ou un élément dans un ligne avec tableau[i][j]
    return tableau


def ouvrir_un_csv_simple(fichier):
    with open(fichier, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)


def devine_header_csv(fichier):
    with open(fichier, 'r') as csvfile:
        test = csvfile.read()
        headers = csv.Sniffer().has_header(test)
        print(headers)
        dialect_deduit = csv.Sniffer().sniff(test)
        reader = csv.reader(csvfile, dialect_deduit)
        for row in reader:
            print(row)
