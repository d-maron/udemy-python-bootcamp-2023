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
        self.view = f'Player #{self.number} \'{self.name}\' has {self.chips} '\
               f'chips'

    def draw_card(self, num=1):
        for n in range(0, num):
            self.hand.append(deck.cards.pop())



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

    for p in num:
        p.draw_card(2)


def place_bet(pnum):
    plyr = players[pnum]
    valid = None
    while not valid:
        valid = input(f'{plyr.name}, what is your bet? ')
        if valid.isdigit():
            valid = int(valid)
            if valid <= plyr.chips:
                plyr.bet += valid
                plyr.chips -= valid
                break

        valid = None
        print(f'Please enter a valid wager up to {plyr.chips}')


# INITIAL SETUP
players = Player('Dealer', 0)
get_players()

deck = Deck()
deck.shuffle()
deal(len(players))

for p in players:
    print(p)

place_bet(1)
print(players[0].bet)
for p in players:
    p.view()
