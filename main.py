import pygame
import os
import random as rd

captain_image = pygame.image.load('captain.png')
captain = pygame.transform.scale(captain_image, (626, 919))
assassin_image = pygame.image.load('assassin.png')
duke_image = pygame.image.load('duke.png')

card_list = ['Captain', 'Ambassador',
             'Inquisitor', 'Contessa',
             'Assassin', 'Duke']


class Deck:
    def __init__(self):
        self.cards = []
        for card in card_list * 3:
            self.cards.append(card)
        rd.shuffle(self.cards)

    def deal_card(self):
        card = self.cards[0]
        self.cards.remove(card)
        return card

    def show_deck(self):
        return print(self.cards)


class Player:
    def __init__(self, player_1_text, first, second):
        self.name = player_1_text
        self.health = 2
        self.bank = 2
        self.card_1 = first
        self.card_2 = second

    def lose_card(self):
        if self.card_1 is not None and self.card_2 is not None:
            choice = input("Which card would you like to lose (1 or 2): ")
            if choice == '1':
                self.card_1 = None
            else:
                self.card_2 = None
        else:
            self.card_1 = None
            self.card_2 = None
            return print("Game over")

    def income(self):
        self.bank += 1
        return print("+1 Coin")

    def foreign_aid(self):
        self.bank += 2
        return print("+2 Coins")

    def inquisitor(self):
        new_card = deck.deal_card()
        print(new_card)
        choice = input("(1 or 2 or No): ")
        if choice == '1':
            self.card_1 = new_card
        elif choice == '2':
            self.card_2 = new_card
        else:
            pass

    def duke(self):
        self.bank += 3
        return print("+3 Coins")

    def ambassador(self):
        tasty = True
        new_card = deck.deal_card()
        while tasty:
            choice = input("(1 or 2): ")
            if choice == '1':
                self.card_1 = new_card
                tasty = False
            elif choice == '2':
                self.card_2 = new_card
                tasty = False
            else:
                pass

    def captain(self):
        choice = input("Who are you captaining (p1 or p2): ")
        if choice == 'p1':
            print(" ")
            block = input("")
            game.player1.bank -= 2
            self.bank += 2
            print("You have successfully captained player 1 (+2 Coins)")
        elif choice == 'p2':
            game.player2.bank -= 2
            self.bank += 2
            print("You have successfully captained player 2 (+2 Coins)")
        else:
            pass

    def assassin(self):
        choice = input("Who are you assassinating (p1 or p2): ")
        if self.bank >= 3:
            if choice == 'p1':
                game.player1.health -= 1
                game.player1.lose_card()
                self.bank -= 3
                print("You have successfully assassinated player 1")
            elif choice == 'p2':
                game.player2.health -= 1
                game.player2.lose_card()
                self.bank -= 3
                print("You have successfully assassinated player 2")
            else:
                pass
        else:
            print("You are broke do something else")

    def show_hand(self):
        return print(self.name + '- ' + self.card_1, self.card_2, self.health, self.bank)


# -------------------------------------------------------------------------------------------------------


class Game:
    def __init__(self):
        self.turn = 1
        self.player1 = Player("Player1", deck.deal_card(), deck.deal_card())
        self.player2 = Player("Player2", deck.deal_card(), deck.deal_card())

    def play(self):
        print("Player 1 starts")
        print(f' ')
        while self.player1.health >= 1 and self.player2.health >= 1:
            player_1 = True
            player_2 = False
            while player_1:
                print("Player 1's turn")
                print(f'\n')
                choice = input("Action: ")
                if choice == "Income":
                    self.player1.income()
                    self.turn += 1
                    player_1 = False
                    player_2 = True
                elif choice == "Foreign Aid":
                    self.player1.foreign_aid()
                    self.turn += 1
                    player_1 = False
                    player_2 = True
                elif choice == "Inquisitor":
                    self.player1.inquisitor()
                    self.turn += 1
                    player_1 = False
                    player_2 = True
                elif choice == "Ambassador":
                    self.player1.ambassador()
                    self.turn += 1
                    player_1 = False
                    player_2 = True
                elif choice == "Duke":
                    self.player1.duke()
                    self.turn += 1
                    player_1 = False
                    player_2 = True
                elif choice == "Captain":
                    self.player1.captain()
                    self.turn += 1
                    player_1 = False
                    player_2 = True
                elif choice == "Assassin":
                    self.player1.assassin()
                    self.turn += 1
                    player_1 = False
                    player_2 = True
                else:
                    print("Invalid choice. Try again")

            while player_2 and player_1 == False:
                print("Player 2's turn")
                choice = input("Action: ")
                if choice == "Income":
                    self.player2.income()
                    self.turn += 1
                    player_2 = False
                    player_1 = True
                elif choice == "Foreign Aid":
                    self.player2.foreign_aid()
                    self.turn += 1
                    player_2 = False
                    player_1 = True
                elif choice == "Inquisitor":
                    self.player2.inquisitor()
                    self.turn += 1
                    player_2 = False
                    player_1 = True
                elif choice == "Ambassador":
                    self.player2.ambassador()
                    self.turn += 1
                    player_2 = False
                    player_1 = True
                elif choice == "Duke":
                    self.player2.duke()
                    self.turn += 1
                    player_2 = False
                    player_1 = True
                elif choice == "Captain":
                    self.player2.captain()
                    self.turn += 1
                    player_2 = False
                    player_1 = True
                elif choice == "Assassin":
                    self.player2.assassin()
                    self.turn += 1
                    player_2 = False
                    player_1 = True
                else:
                    print(f'\n')
                    print("Invalid choice. Try again")

    # --------------------------------------------------------------------------------------------------------------------


deck = Deck()
game = Game()

game.play()
