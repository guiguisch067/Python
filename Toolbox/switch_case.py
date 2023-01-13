#! python3

# On teste la fonctionnalité match, équivalent à switch;case

string = input("Entrez un mot : ")

match string:
    case "Ping":
        print("Pong")
    case "Pong":
        print("Ping")

print("Bonjour !")