"""
BLACKJACK card game
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
faces = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}
game_on = True

# DEFINE CLASSES
class Card:

    def __init__(self, face, suit):
        self.suit = suit
        self.face = face
        self.value = values[face]

    def __str__(self):
        return f'{self.face} of {self.suit} ({self.value})'


class Deck:

    def __init__(self):

        self.cards = []
        for suit in suits:
            for face in faces:
                self.cards.append(Card(face, suit))

    def __str__(self):

        return str(len(self.cards))

    def shuffle(self):

        random.shuffle(self.cards)


class Player:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.hand = []
        self.chips = 100
        self.bet = 0

    def draw_card(self, num=1):
        for n in range(0, num):
            self.hand.append(deck.cards.pop())

    def place_bet(self):
        valid = None
        while not valid:
            valid = input(f'{self.name}, what is your bet? ')
            if valid.isdigit():
                valid = int(valid)
                if valid <= self.chips:
                    self.bet += valid
                    self.chips -= valid
                    break
            valid = None
            print(f'Please enter a valid wager up to {self.chips}')

    def view(self):
        print(f'Player #{self.number} \'{self.name}\' has {self.chips} '
               f'chips')



def howmanyplayers():
    promptvalid = False
    howmany = 0
    while not promptvalid:
        howmany = input("How many people are playing? ")
        if howmany.isdigit() and int(howmany) in range(1, 10):
            howmany = int(howmany)
            break
        else:
            print("Please enter 1 - 9 players")

    print(f'{howmany} players selected')
    return int(howmany)


def get_players():
    tmp = [Player('Dealer', 0)]
    n = howmanyplayers()
    for i in range(1, n + 1):
        name = ''
        while not name:
            name = input(f'Enter player {i}\'s name: ')
        tmp.append(Player(name, i))
    return tmp


def deal(num):
    for p in range(0, num):
        players[p].draw_card(2)


# INITIAL SETUP
players = Player('Dealer', 0)
players = get_players()
players[0].chips = 0    # Dealer has no chips

deck = Deck()
deck.shuffle()
deal(len(players))

players[1].place_bet()
print(players[0].bet)
for p in players:
    p.view()