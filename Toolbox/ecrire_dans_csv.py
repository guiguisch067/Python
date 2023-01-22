#! python3
# manipulations de fichiers permettant d'avoir la liste d'application, avec le nom du PC et celui de l'utilisateur

import csv

def ecrire_dans_csv():
    # field names
    fields = ['Name', 'Branch', 'Year', 'CGPA']
    
    # data rows of csv file
    rows = [ ['Nikhil', 'COE', '2', '9.0'],
            ['Sanchit', 'COE', '2', '9.1'],
            ['Aditya', 'IT', '2', '9.3'],
            ['Sagar', 'SE', '1', '9.5'],
            ['Prateek', 'MCE', '3', '7.8'],
            ['Sahil', 'EP', '2', '9.1']]
    
    # name of csv file
    filename = "university_records.csv"
    
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        
        # writing the fields
        csvwriter.writerow(fields)
        
        # writing the data rows
        csvwriter.writerows(rows) 

def ecrire_dans_csv_basique():
    # utiliser l'option ,'a' pour "append" et rajouter une ligne dans le fichier
    # plutot que de le réécrire complètement
    with open("vulns.csv", 'w') as csvfile:
        write_csv = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write_csv.writerow(['9944461111333337',"rip en piece"])

if __name__ == "__main__":
   ecrire_dans_csv_basique()