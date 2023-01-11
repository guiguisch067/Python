#! python3

def tableau_vers_dico(tableau, key_column):
    # créer une liste de dictionnaires en rapport avec la longueur du tableau
    dict_list = [{tableau[0][i]: ligne[i] for i in range(len(ligne))} for ligne in tableau[1:]]

    # créer un dictionnaire avec les colonnes (1ere ligne en général, donc valeur 0 du tableau correspondant à la clé
    # et un dictionnaire avec la valeur des colonnes comme clé, et les dictionaires comme valeurs
    result = {ligne[key_column]: ligne for ligne in dict_list}

    return result


def table_to_dict(table, key_column):
    # create a list of dictionaries
    dict_list = [{table[0][i]: row[i] for i in range(len(row))} for row in table[1:]]

    # create a dictionary with the key column as the keys and the dictionaries as the values
    result = {row[key_column]: row for row in dict_list}

    return result

'''
example usage
tableau = [
    ['id', 'name', 'age'],
    [1, 'Alice', 20],
    [2, 'Bob', 30],
    [3, 'Eve', 25]
]

dict_by_id = tableau_vers_dico(tableau, 0)
print(dict_by_id)

# output:
# {1: {'id': 1, 'name': 'Alice', 'age': 20},
#  2: {'id': 2, 'name': 'Bob', 'age': 30},
#  3: {'id': 3, 'name': 'Eve', 'age': 25}}
'''


def create_dict_keys(table):
    # get the first row of the table (the header row)
    header_row = table[0]

    # create an empty dictionary
    keys = {}

    # iterate over the items in the header row
    for i, item in enumerate(header_row):
        # add each item as a key in the dictionary, with the index as the value
        keys[item] = i

    return keys


'''
# example usage
table = [['Name', 'Age', 'Gender'], ['Alice', '23', 'Female'], ['Bob', '35', 'Male']]
keys = create_dict_keys(table)
print(keys)  # Output: {'Name': 0, 'Age': 1, 'Gender': 2}
'''

def create_dict_keys_2(table):
    # get the first row of the table as the list of keys
    keys = table[0]

    # create a dictionary for each row in the table using a dictionary comprehension
    dict_list = [dict(zip(keys, row)) for row in table[1:]]

    return dict_list

'''
# example usage
table = [
    ['id', 'name', 'age'],
    [1, 'Alice', 20],
    [2, 'Bob', 25],
    [3, 'Charlie', 30],
]
dict_list = create_dict_keys(table)
print(dict_list)
'''