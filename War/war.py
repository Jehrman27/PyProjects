"""
Two computer players compete in a card game of War.
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
            'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12,
            'King':13, 'Ace':14}


class Card:
    """ Creates Card object with suit and rank."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    """ Creates Deck object made of Card objects.

    .shuffle() -- randomly reorders the Deck object.
    .deal_one() -- removed and returns the last Card object.
    """

    def __init__(self):
        self.all_cards =[]

        for suit in suits:
            for rank in ranks:
                # Create the Card object.
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        """ Randomly reorders the Deck object."""
        random.shuffle(self.all_cards)

    def deal_one(self):
        """ Removed and returns the last Card object."""
        return self.all_cards.pop()


class Player():
    """ Creates Player object that holds Card objects.

    .remove_one() -- removes and returns the first Card object.
    .add_cards() -- adds one or more Card objects to the Player object.
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        """ Removes and returns the first Card object."""
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """ Adds one or more Card objects to the Player object."""
        if isinstance(new_cards, list):
            # List of multiple Card objects.
            self.all_cards.extend(new_cards)
        else:
            # A single Card Object.
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

GAME_ON = True
ROUND_NUM = 0

while GAME_ON:

    ROUND_NUM += 1
    print(f"Round {ROUND_NUM}")

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two wins!")
        GAME_ON = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One wins!")
        GAME_ON = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    AT_WAR = True

    while AT_WAR:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            AT_WAR = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            AT_WAR = False

        else:
            print("War!")

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war.")
                print("Player Two wins!")
                GAME_ON = False
                break

            if len(player_two.all_cards) < 5:
                print("Player Two unable to declare war.")
                print("Player One wins!")
                GAME_ON = False
                break

            for num in range(5):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())
