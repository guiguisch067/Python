#! python3

# On teste la fonctionnalit√© match, √©quivalent √† switch;case

string = input("Entrez un mot : ")

match string:
    case "Ping":
        print("Pong")
    case "Pong":
        print("Ping")

print("Bonjour !")