#! pyton3
# algortihme permettant de choisir une position dans une matrice ave cune entrée utilisaeur simple
# l'utilisateur choisit une valeur de 1 à 9
# la matrice est composée d'une liste, contenant 3 listes, de 3 éléments.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

position = int(input("Please enter a position between 1 and 9: "))

row = (position-1) // 3
col = (position-1) % 3
element = matrix[row][col]

print(element)
