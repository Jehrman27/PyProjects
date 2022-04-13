"""
Play BlackJack against a computer player.
"""
from random import shuffle
from time import sleep
import os
import sys

suits = ('♥', '♦', '♣', '♠')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
            'J':10, 'Q':10, 'K':10, 'A':11}


class Card:
    """Creates Card object with suit and rank."""


    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]


    def __str__(self):
        return self.rank + self.suit


class Deck:
    """Creates Deck object made of Card objects.

    .shuffle() -- randomly reorders the Deck object.
    .deal_one() -- removed and returns the last Card object.
    """


    def __init__(self):
        """Call reset to initialize deck"""
        self.all_cards = []
        self.reset()


    def shuffle(self):
        """ Randomly reorders the Deck object."""
        clear_screen()
        shuffle(self.all_cards)
        print("Shuffling deck.")
        sleep(.5)
        clear_screen()
        print("Shuffling deck..")
        sleep(.5)
        clear_screen()
        print("Shuffling deck...")
        sleep(.5)
        clear_screen()


    def reset(self):
        """Resets deck to original 52 cards."""
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create the Card object.
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)


    def deal_one(self):
        """Removed and returns the last Card object."""
        return self.all_cards.pop()


class Hand:
    """Creates a Hand object for holding a player's Card objects"""

    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.sum_of_cards = 0


    def __str__(self):
        card_list = ''
        for card in self.all_cards:
            card_list += (" " + card.rank + card.suit)
        return self.name + "'s hand:\n" + card_list + "\n"


    def add_card(self, card):
        """Adds card to list of cards in Hand."""
        self.all_cards.append(card)
        self.sum_of_cards += card.value


    def discard(self):
        """Discards all Card objects in Hand."""
        self.all_cards = []
        self.sum_of_cards = 0


    def dealer_hidden(self):
        """Displays the dealer's hand with the second card covered."""
        first_card = self.all_cards[0].rank + self.all_cards[0].suit
        return "Dealer's hand:\n " + first_card +" **\n"


class Chips:
    """Creates a chip bank object for the player to use for betting.

    bank -- The player's starting balance of chips.
    """

    def __init__(self, bank):
        self.bank = bank

    def total(self):
        """Returns the total chips in the Player's bank."""
        return self.bank

    def bet(self, chips):
        """Returns bool if there's enough chips to bet and removes
            if there is.
        """
        if chips > self.bank:
            return False
        self.bank -= chips
        return True

    def add_chips(self, chips):
        """Adds chips to the player's bank."""
        self.bank += chips


class Player:
    """Creates a Player object to track the player's stats."""

    def __init__(self, name):
        self.name = name
        self.hands_won = 0
        self.hands_lost = 0
        self.hands_pushed = 0
        self.chips_bet = 0
        self.chips_won = 0
        self.bank = Chips(100)


    def win(self):
        """Increments games won."""
        self.hands_won += 1


    def lose(self):
        """Increments games lost."""
        self.hands_lost += 1


    def tied(self):
        """Increments games pushed."""
        self.hands_pushed += 1


    def bets(self, bet):
        """Adds bet to current total of bets."""
        self.chips_bet += bet


    def winnings(self, net):
        """Adds wins or losses to current total."""
        self.chips_won += net


def clear_screen():
    """Identifies the running OS and clears the terminal."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def player_input(prompt, case_sens, *args):
    """Returns validated user input.

    prompt -- what to ask user when pulling response.
    case_sens -- if validation should consider casing.
    *args -- valid user responses to check for.
    """
    ans = ''
    valid_inputs = [str(item) for item in args]
    if case_sens:
        while str(ans) not in valid_inputs:
            ans = input(prompt)
            if ans not in valid_inputs:
                print('Not a valid response.')
    else:
        while ans.casefold() not in valid_inputs:
            ans = input(prompt)
            ans = ans.casefold()
            if ans not in valid_inputs:
                print('Not a valid response.')
    return ans


def hit_or_stay():
    """Returns player's decision for their hand."""
    return player_input("(1) -- Hit\n(2) -- Stay\nChoose: ", False, "1", "2")


def check_hand(hand_obj):
    """Takes in a Hand object and returns the sum of the Cards within
    and boolean if the hand busted.

    """
    hand_sum = 0
    hand_bust = False
    hand_sum = hand_obj.sum_of_cards

    check_bust = True
    while check_bust:
        if hand_sum > 21:
            for card in hand_obj.all_cards:
                if card.rank == "A":
                    hand_sum -= 10
                    continue
            if hand_sum > 21:
                hand_bust = True
        check_bust = False

    return hand_bust


def draw_board(hide=True):
    """Displays the cards in the dealer's and player's hands."""
    clear_screen()
    if hide:
        print(dealer_hand.dealer_hidden())
    else:
        print(dealer_hand)
    print(player_hand)


def play_round():
    """Starts a round of BlackJack."""
    clear_screen()
    # player bet
    while True:
        print("Available chips for betting: " + str(player.bank.total()))
        bet = input("How much would you like to bet?")
        try:
            bet = int(bet)
        except:
            print("Invalid entry.")
            continue
        if not player.bank.bet(bet):
            print("You don't have enough chips to bet that much.")
            continue
        player.chips_bet += bet
        break

    # shuffle deck
    if len(deck.all_cards) == 52 or len(deck.all_cards) < 26:
        deck.shuffle()
        #print(len(deck.all_cards))
        input("Shuffling complete. Press Enter to deal.")

    # deal
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    # player plays hand
    player_turn = True
    dealer_turn = True
    while player_turn:
        draw_board(True)
        if hit_or_stay() == "1":
            print("Hit!")
            player_hand.add_card(deck.deal_one())
        else:
            print("Stay!")
            player_turn = False
        if check_hand(player_hand):
            draw_board(True)
            player_turn = False
            dealer_turn = False
            
    # dealer plays
    while dealer_turn:
        draw_board(False)
        if dealer_hand.sum_of_cards < 17:
            print("The dealer hits...")
            sleep(1)
            dealer_hand.add_card(deck.deal_one())
        elif dealer_hand.sum_of_cards > 21:
            print("Dealer bust! Congrats, you win this hand!")
            player.hands_won += 1
            player.bank.add_chips(bet*2)
            dealer_turn = False
        else:
            print("The dealer stays...")
            sleep(1)
            dealer_turn = False

    # compare and payout
    if check_hand(player_hand):
        print("Bust! You lost your bet.")
        player.hands_lost += 1
    elif dealer_hand.sum_of_cards > 21:
        player.hands_won += 1
        player.bank.add_chips(bet*2)
    elif dealer_hand.sum_of_cards == player_hand.sum_of_cards:
        print("Push! Get your bet back.")
        player.hands_pushed += 1
        player.bank.add_chips(bet)
    elif dealer_hand.sum_of_cards > player_hand.sum_of_cards:
        print("The dealer beat your hand. You lost your bet.")
        player.hands_lost += 1
    else:
        print("Congrats, you beat the dealer! You win your bet.")
        player.hands_won += 1
        player.bank.add_chips(bet*2)

    # discard cards
    dealer_hand.discard()
    player_hand.discard()

    # ask to play again
    if player_input("Would you like to play another hand? (y/n): ",
         False, "y", "n") == "y":
        play_round()
    else:
        main_menu()
    # print(check_hand(player_hand))


def instructions():
    """Displays instructions to the player."""
    clear_screen()
    print("How to play:\n")
    print("Every round you will start by placing your bet.")
    print("You will be dealt two face-up cards.")
    print("The dealer will be dealt one card face-down and one face-up.")
    print("Your goal is to get closer to 21 than the dealer without going"
            "over.")
    print("As long as your cards add up to less than 21, you can "
            "'hit' to get another card.")
    print("If you go over 21 (bust), you lose the round immediately.")
    print("If you stay with 21 or less, the dealer will play his hand,"
            "trying to beat your hand.")
    print("If you and the dealer end with the same sum, you get "
            "your bet back (push).")
    input("\nPress Enter to return to the main menu.")
    main_menu()


def player_stats():
    """Displays the player's statistics."""
    clear_screen()
    print(f"Statistics for {player.name}:\n")
    print(f"Hands won:     {player.hands_won}")
    print(f"Hands lost:    {player.hands_lost}")
    print(f"Hands pushed:  {player.hands_pushed}")
    print(f"Chips bet:     {player.chips_bet}")
    print(f"Chips won:     {player.chips_won}")
    print(f"Total chips:   {player.bank.total()}")
    input("\nPress Enter to return to the main menu.")
    main_menu()


def main_menu():
    """Displays main menu. Calls user's selection."""
    clear_screen()
    print("Main Menu:\n")
    print("(p) -- play")
    print("(i) -- instructions")
    print("(s) -- stats")
    print("(q) -- quit")
    user_choice = player_input("\nPlease choose an option: ",
                                False,
                                "p", "i", "s", "q")

    if user_choice == "p":
        play_round()
    elif user_choice == "i":
        print("instructions")
        instructions()
    elif user_choice == "s":
        player_stats()
    else:
        print("Thanks for playing!")
        sys.exit()


clear_screen()
print("Welcome to BlackJack!\n")
print("You will be competing against the computer to get as close",
        "to 21 without going over.\n")
player = Player(input("Please enter your name: "))
deck = Deck()
dealer_hand = Hand("Dealer")
player_hand = Hand(player.name)
main_menu()
