class Etudiant:
    def __init__(self, nom, niveau, moyenne, diplome_ok):
        self.nom = nom
        self.majniveauor = niveau
        self.moyenne = moyenne
        self.diplome_ok = diplome_ok

    # on définie une fonction au sein de la classe
    def afficher_Classe(self):
        print(self.nom, self.majniveauor, self.moyenne, self.diplome_ok)


# alternative
def afficher(student: Etudiant):
    print(student.nom)


#On créé un objet etudiant1 de type Etudiant
etudiant1 = Etudiant("Guillaume", "BACplus5", "B", True)


# Cet appel utilise l'objet etudiant1 de type Etudiant avec la fonction au sein de la classe
etudiant1.afficher_Classe() 


# alternative : cet appel utilise une fonction classique, hors classe, avec un paramêtre un objet de type etudiant
afficher(etudiant1)