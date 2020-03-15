"""A Game of black jack

Classes:
    Card: Each Card object has attributes value and suite.
    Deck: Each Deck object contains a list of Card objects.
    Player: Has attributes like player's hand and chips.
    Dealer: Inherits from Player class and modifies method show_hand

Functions:
    clrscr() -> None: Clears the screen.
    print_intro() -> None: Prints the game introduction.
    place_bets(Player) -> None: Receives bet from Player and modify Player.bet
    play_again() -> None: Receives player input if he wants to play again.
    game() -> None: Main driver function.
"""

import random
import os
import time


class Card:
    """Used to instantiate cards in deck.

    Attributes:
        value(str): the value of card, 'A', 'J', '2', '10', etc
        suite(str): the suite to which card belongs, 'hearts', 'spades', etc

    Methods:
        __init__: __init__ method for Card class
        __str__: Returns the value and suite of card objects
    """

    def __init__(self, value: str, suite: str) -> None:
        """The __init__ method for Card class

        Args:
            value: the value of card, 'Ace', 'Jack', 'Two', 'Ten', etc
            suite: the suite to which card belongs, 'Hearts', 'Spades', etc
        """
        self.value = value
        self.suite = suite

    def __str__(self) -> str:
        """Returns the value and suite of Card object."""
        return self.value + ' of ' + self.suite


class Deck:
    """Used to instantiate new decks of cards.

    Attributs:
        card_values: list of possible values of cards, 'One', 'Ace', etc
        suites: list of possible suites for cards, 'Hearts', 'Spades', etc
        cards: list of cards present in the deck

    Methods:
        __init__: creates a new Deck object
        __str__: returns all cards in deck
        __len__: returns the number of cards in Deck
        shuffle: shuffles the deck
    """
    card_values = [
        'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',
    ]
    suites = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

    def __init__(self) -> None:
        """Creates a new deck."""
        self.cards = list()
        for suite in Deck.suites:
            for value in Deck.card_values:
                self.cards.append(Card(value, suite))   # Card objects

    def __str__(self) -> str:
        """Returns all the cards in deck."""
        return str([str(card) for card in self.cards])

    def __len__(self) -> int:
        """Returns the number of cards in deck."""
        return len(self.cards)

    def shuffle(self) -> None:
        """Shuffles the deck."""
        random.shuffle(self.cards)


class Player:
    """The methods and attributes of the player.

    Attributes:
        hand: the list of cards in players hand
        turn: bool to check if it is player's turn
        hand_value: value of player's hand when last calculted
        chips: chips avilable to the player initialized to 1000
        bet: bet placed by the player initialized to 100

    Mehods:
        __init__: creates an empty hand list for player
        hit: adds a new card to player's hand and update hand_value
        calcute_hand: updates the player's hand_value
        show_hand: prints the cards in player's hand
        draw_cards: Initializes a new list for hand and add two cards
    """
    def __init__(self) -> None:
        """__init__ method for Player objects.
        """
        self.turn = False
        self.chips = 1000
        self.bet = 100
        self.hand = list()
        self.hand_value = 0

    def draw_cards(self, playing_deck: Deck) -> None:
        """Initializes a new list for hand and add two cards

        Args:
            playing_deck: the current deck of cards
        """
        self.hand = list()
        self.hit(playing_deck)
        self.hit(playing_deck)

    def hit(self, playing_deck: Deck) -> None:
        """Add the given card to the hand of player.

        Args:
            playing_deck: the present deck of cards
        """
        card = playing_deck.cards.pop()
        self.hand.append(card)
        self.calculate_hand()

    def calculate_hand(self) -> None:
        """Updates the value of player's hands_value"""
        total = flag = 0
        # Calcuting values for each card.
        for card in self.hand:
            value = Deck.card_values.index(card.value) + 1
            if 1 < value < 10:
                total += value
            elif value >= 10:
                total += 10
            elif value == 1:
                flag += 1
        # Calculating value of 'Ace'
        while flag:
            if total+11 > 21:
                total += 1
            else:
                total += 11
            flag -= 1

        self.hand_value = total

    def show_hand(self):
        """Prints the card's in player's hand"""
        time.sleep(1)
        print(f"Player's Hand: \t {self.hand_value}")
        for card in self.hand:
            print(f"   {card}")
        print()


class Dealer(Player):
    """Methods and attributes of Dealer.

    Parent class:
        Player: Inherits all methods and attributes from Player class

    Attributes:

    Methods:
        show_hand: prints the cards in dealer's hand
    """
    def show_hand(self) -> None:
        """Prints the dealer's cards"""
        if not self.turn:
            print(f"Dealer's Hand: Unknown")
            print(f"   {self.hand[0]}")
            print("   <Hidden>")
            print()
        else:
            time.sleep(1)
            print(f"Dealer's Hand: \t {self.hand_value}")
            for card in self.hand:
                print(f"   {card}")
            print()


def clrscr() -> None:
    """Clears the screen"""
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def print_intro() -> None:
    """Prints the game introduction"""
    print("""\t\tWelcome to BlackJack!
    Get as close to 21 as you can without going over!
    Dealer hits until she reaches 17. Aces count as 1 or 11.
    """)


def place_bets(player: Player) -> None:
    """Recieve the bet from player.
    
    Args:
        player: Player who is placing the bets
    """
    while True:
        try:
            bet = int(input("Enter your bet: (Minimum bet: 100 chips)\n"))
            if 100 <= bet <= player.chips:
                player.bet = bet
                break
            else:
                print("Enter valid bet")
        except:
            print("Enter valid bet")
            

def play_again() -> None:
    """Asks if the player wants to play again
	Starts a new game if the player selects 'y'
    """
    time.sleep(2)
    print("\nDo you want to play again? (y/n)")
    if input().lower().startswith('y'):
        if player1.chips >= 100:
            game()
        else:
            print("\nSorry! Not enough chips!")
            quit()
    else:
        print("Thanks for playing!")
        quit()


dealer = Dealer()
player1 = Player()

def game() -> None:
    """Main driver function."""
    clrscr()
    print_intro()
    playing_deck = Deck()
    playing_deck.shuffle()

    print(f"Avilable chips: {player1.chips}")
    place_bets(player1)

    # Dealing cards from deck.
    dealer.draw_cards(playing_deck)
    player1.draw_cards(playing_deck)
    dealer.turn = False
    player1.turn = True
    dealer.show_hand()
    player1.show_hand()

    # Player playing.
    while player1.turn:
        print("Do you want to:")
        print("1.Hit \t 2.Stay")
        choice = input()

        if choice.lower().startswith('2') or choice.lower().startswith('s'):
            player1.turn = False
        elif choice.lower().startswith('1') or choice.lower().startswith('h'):
            player1.hit(playing_deck)
        else:
            print("Enter valid choice:")
            continue

        player1.show_hand()
        if player1.hand_value > 21:
            print("BUST!! Dealer won")
            player1.chips -= player1.bet
            print(f"Avilable chips: {player1.chips}")
            play_again()

    # Dealer playing.
    dealer.turn = True
    dealer.show_hand()
    while (dealer.hand_value <= 17) and (dealer.hand_value <= player1.hand_value):
        dealer.hit(playing_deck)
        dealer.show_hand()

    # Chosing the winner
    if dealer.hand_value > 21 or dealer.hand_value < player1.hand_value:
        print("\nCongratulations! You won!")
        player1.chips += player1.bet
    elif dealer.hand_value == player1.hand_value:
        print("\nPush!")
    else:
        print("\nDealer won.")
        player1.chips -= player1.bet
    print(f"Avilable chips: {player1.chips}")

    play_again()


if __name__ == '__main__':
    game()
