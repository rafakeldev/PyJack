# BlackShrek Python Script 3.10.0 Created By Rafael & Wassim

import random

# Stock le total de gain ou perte du joueur
totalReport = 0


# Déclaration des fonctions

def afficher_regles():
    """Affiche les règles du BlackShrek"""
    print("Le concept du BlackShrek c'est de se rapprocher de 21 (SANS le dépasser).\n"
          "Au début vous recevez deux cartes, si vous obtenez 21 à ce tour alors vous avez BlackShrek.\n"
          "Vous devez avoir un score plus élevé que l'Âne.\n\n"
          "/!\\ L'Âne n'arrête pas de tirer une carte tant qu'il n'a pas atteint 17 /!\\\n")

    print("| Gain |\n"
          "| x1 | si vous gagnez une partie.\n"
          "| x2 | si vous obtenez un BLACKSHREK\n"
          "| x0 | si vous êtes à égalité avec l'Âne)\n")


def distribuer(deck):
    """
    Distribue deux cartes du paquet à une personne.
            Parameters:
                deck (list): Paquet de carte du jeu
            Return:
                hand (list): Jeu d'une personne
    """
    hand = []
    for i in range(2):
        random.shuffle(deck)
        tirer(hand, deck)
    return hand


def rejouer(wallet):
    """
    Propose au joueur si il veut refaire une partie.
            Parameters:
                wallet (int): Solde du joueur
            Return:
                Nothing
    """

    choice = input("Shrek te propose de rejouer? (O/N) : ").lower()
    if choice == "o":
        game(wallet)
    else:
        print("Merci d'avoir joué à notre BlackShrek!")
        # Affiche le résultat des pertes/gains du joueur
        if totalReport < 0:
            print("Vous avez perdu " + str(-totalReport) + "€")
        elif totalReport >= 0:
            print("Vous avez gagné " + str(totalReport) + "€")
        exit()


def total(hand):
    """
    Calcule le total du jeu d'une personne.
            Parameters:
                hand (list): Jeu d'une personne
            Return:
                total_score (int): Le score total de la personne par rapport à son jeu
    """

    total_score = 0
    for card in hand:
        if card == "V" or card == "D" or card == "R":
            total_score += 10
        elif card == "A":
            if total_score >= 11:
                total_score += 1
            else:
                total_score += 11

        else:
            total_score += card
    return total_score


def definir_solde(bet, total_money, action, multiplier=0):
    """
    Calcule le solde du joueur après avoir misé.
            Parameters:
                bet (int): Mise du joueur
                total_money (int): Solde du joueur
                action (str): Action de la fonction si elle rajoute ou retire de l'argent
                multiplier (int): Multiplicateur du gain (si le joueur obtient un gain d'argent) (Default value of 0)
            Return:
                total_money - bet (int): Solde restant du joueur
    """
    global totalReport
    if action == "retirer":
        totalReport -= bet
        return total_money - bet
    elif action == "ajouter":
        totalReport += bet * multiplier
        return total_money + bet * multiplier


def tirer(hand, deck):
    """
    Ajoute une carte au jeu d'une personne.
            Parameters:
                hand (list): Jeu d'une personne
                deck (list): Paquet de carte du jeu
            Return:
                hand (list): Jeu d'une personne
    """

    # Retire une carte du paquet.
    card = deck.pop()
    if card == 11:
        card = "V"
    if card == 12:
        card = "D"
    if card == 13:
        card = "R"
    if card == 14:
        card = "A"

    # Ajoute la carte dans le jeu définit par hand()
    hand.append(card)
    return hand


def afficher_resultats(player_hand, dealer_hand):
    """
    Affiche le résultat du croupier et du joueur.
            Parameters:
                player_hand (list): Jeu du joueur
                dealer_hand (list): Jeu du croupier
            Return:5
                Nothing
    """

    print("L'Âne a un " + str(dealer_hand) + " pour un total de " + str(total(dealer_hand)))
    print("Le joueur a un " + str(player_hand) + " pour un total de " + str(total(player_hand)) + "\n")


def blackshrek(player_hand, dealer_hand, wallet, bet):
    """
    Vérifie si le joueur ou l'Âne a obtenu un BlackShrek.
            Parameters:
                player_hand (list): Jeu du joueur
                dealer_hand (list): Jeu du croupier
                wallet (int): Solde du joueur
                bet (int): Mise de départ du joueur
            Return:
                Nothing
    """

    if total(player_hand) == 21:
        afficher_resultats(player_hand, dealer_hand)
        print("Incroyable! Vous avez un BLACKSHREK!!!\n")
        wallet = definir_solde(bet, wallet, "ajouter", 3)
        print("Vous avez maintenant " + str(bet * 3) + " en plus sur votre solde!\n"
                                                       "Solde: " + str(wallet) + "\n")
        rejouer(wallet)

    elif total(dealer_hand) == 21:
        afficher_resultats(player_hand, dealer_hand)
        print("Vous avez perdu. L'Âne a un BLACKSHREK!!!\n"
              "Solde: " + str(wallet))
        rejouer(wallet)

    elif total(player_hand) == 21 and total(dealer_hand) == 21:
        print("Vous et l'Âne avez obtenu un BLACKSHREK! VOus ne gagnez donc rien mais vous ne perdez rien.\n")
        wallet = definir_solde(bet, wallet, "ajouter", 1)
        rejouer(wallet)


def score(player_hand, dealer_hand, wallet, bet):
    """
    Calcule le score du joueur et du croupier.
        Parameters:
            player_hand (list): Jeu du joueur
            dealer_hand (list): Jeu du croupier
            wallet (int): Solde du joueur
            bet (int): Mise du joueur
        Return:
            Nothing
    """

    # Si le score du joueur est > 21 et que l'Âne à un score <= 21 alors le joueur perd.
    if total(player_hand) > 21 and total(dealer_hand) <= 21:
        afficher_resultats(player_hand, dealer_hand)
        print("Vous avez brulé!\n"
              "Solde: " + str(wallet))

    # Si le score du croupier est > 21 et que le joueur à un score <= 21 alors le joueur gagne.
    elif total(dealer_hand) > 21 and total(player_hand) <= 21:
        afficher_resultats(player_hand, dealer_hand)
        print("L'Âne a brulé! Vous avez gagné!\n")
        wallet = definir_solde(bet, wallet, "ajouter", 2)
        print("Vous avez maintenant " + str(bet * 2) + " en plus sur votre solde!\n"
                                                       "Solde: " + str(wallet) + "\n")
    # Si le score du joueur est < que le score du croupier alors le joueur perd.
    elif total(player_hand) < total(dealer_hand):
        afficher_resultats(player_hand, dealer_hand)
        print("L'Âne a un score plus élevé. Vous avez perdu!\n"
              "Solde: " + str(wallet))

    # Si le score du joueur est > que le score du croupier alors le joueur gagne.
    elif total(player_hand) > total(dealer_hand):
        afficher_resultats(player_hand, dealer_hand)
        print("Félicitation! Votre score est plus élevé que l'Âne.\n")
        wallet = definir_solde(bet, wallet, "ajouter", 2)
        print("Vous avez maintenant " + str(bet * 2) + " en plus sur votre solde!\n"
                                                       "Solde: " + str(wallet))

    # Si le joueur et le croupier ont brulé alors tout le monde.
    elif total(player_hand) > 21 and total(dealer_hand) > 21:
        afficher_resultats(player_hand, dealer_hand)
        print("Dommage! Vous et l'Âne avez brulé.\n"
              "Solde: " + str(wallet))
    return wallet


def game(wallet):
    """
    Gère tout le système du jeu.
            Parameters:
                wallet (int): Solde du joueur
            Return:
                Nothing
    """

    # Déclaration d'une variable permettant de stocker un jeu complet de cartes. (52)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

    choice = ""
    bet = int(input("Veuillez entrer une mise de départ (€) : "))
    while bet > wallet:
        print("Vous n'avez pas suffisamment d'argent pour miser!\n"
              "Veuillez choisir un montant inférieur...")
        bet = int(input("Veuillez entrer une mise de départ (€) : "))

    wallet = definir_solde(bet, wallet, "retirer")

    # Distribution des cartes
    dealer_hand = distribuer(deck)
    player_hand = distribuer(deck)

    # Boucle qui vérifie si le joueur veut arrêter la partie
    while choice != "q":
        print("L'Âne montre un " + str(dealer_hand[0]))
        print("Vous avez un " + str(player_hand) + " pour un total de " + str(total(player_hand)) + "\n")

        # Vérifie si le joueur ou l'Âne a un BlackShrek
        blackshrek(player_hand, dealer_hand, wallet, bet)

        # Stock le choix du joueur
        choice = input("Voulez-vous [T]irer, [R]ester, ou [Q]uitter: ").lower()

        # Le joueur décide de prendre une carte
        if choice == "t":

            # Le joueur a une carte en plus
            tirer(player_hand, deck)

            # Tant que l'Âne à moins de 17 il continuera à tirer une carte
            if total(dealer_hand) < 17:
                while total(dealer_hand) < 17:
                    tirer(dealer_hand, deck)

            # Afficher les scores
            # Affecter le nouveau solde au wallet
            wallet = score(player_hand, dealer_hand, wallet, bet)

            # Propose au joueur si il veut rejouer
            rejouer(wallet)

        # Le joueur décide de ne pas prendre une autre carte mais continue à jouer
        elif choice == "r":
            if total(dealer_hand) < 17:
                while total(dealer_hand) < 17:
                    tirer(dealer_hand, deck)

            # Afficher les scores et Affecter le nouveau solde au wallet
            wallet = score(player_hand, dealer_hand, wallet, bet)
            rejouer(wallet)

        # Le joueur décide de quitter la partie
        elif choice == "q":
            print("Merci d'avoir joué à notre BlackShrek!")

            # Affiche le résultat des pertes/gains du joueur
            if totalReport < 0:
                print("Vous avez perdu " + str(-totalReport) + "€")
            elif totalReport >= 0:
                print("Vous avez gagné " + str(totalReport) + "€")
            exit()


# Corps du programme

afficher_regles()

print("Bienvenue au Casino Shrek!\n")

money = int(input("Veuillez entrer le montant de votre porte-monnaie (€) : "))

# Limite de solde car une grosse some peut causer des erreurs
if money > 50000:
    while money > 50000:
        print("Vous ne pouvez pas mettre au-delà de 50 000€ dans votre porte-monnaie!\n")
        money = int(input("Veuillez entrer le montant de votre porte-monnaie (€) : "))

game(money)
