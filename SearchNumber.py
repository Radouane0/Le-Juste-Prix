import random

while True:
    prix = random.randint(1, 10)

    tentative = 0

    print("Bienvenue dans Le Juste Prix, à toi de deviner le bon chiffre qui est compris entre 1 et 10.")

    while True:
        nombre = int(input())
        tentative += 1
        if (nombre < prix):
            print("Le chiffre est plus haut")
        elif (nombre > prix):
            print("Le chiffre est plus bas")
        else:
            print(f"Félicitation, vous avez trouvé le bon chiffre en {tentative} tentative(s)")
            break
        
    replay = input("Voulez-vous rejouer ? (oui/non): ")
    if replay.lower() != 'oui':
        print("Partie terminée")
        break       