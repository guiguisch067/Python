#! python3


# On manipule des classes


class Benoit:
    def __init__(self, nom):
        self.nom = nom

    def presentation(self):
        print(f"Je m'appelle {self.nom}")


class Guillaume:
    def __init__(self):
        self.nom = "Guillaume"

    def presentation(self):
        print(f"Je suis {self.nom}")


def main():
    benoit = Benoit("Barnoux")
    guillaume = Guillaume()

    benoit.presentation()
    guillaume.presentation()


main()
