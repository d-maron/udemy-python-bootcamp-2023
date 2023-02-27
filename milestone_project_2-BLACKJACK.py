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

    def __init__(self, name, number, chips=100):
        self.name = name
        self.number = number
        self.cards = []
        self.chips = chips
        self.bet = 0
        self.total = 0

    def view_cards(self):
        print(f'{self.name}\'s cards:')
        for card in self.cards:
            print('    ', card)
        # print(f'{self.name}\'s hand totals {self.total}.')

    def view_chips(self):
        print(f'{self.name} has {self.chips} chips.')

    def draw_card(self, num=1):
        for n in range(0, num):
            self.cards.append(deck.cards.pop())

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

    def choose_move(self):
        choice = ''
        while choice == '':
            tmp = input(f'Player {self.number}, hit or stand? (h/s) ')
            if tmp.lower() == 'h':
                choice = 'hit'
            elif tmp.lower() == 's':
                choice = 'stand'
            else:
                print('Please choose \'h\' or \'s\'.')
        print(f'{self.name} chooses to {choice.upper()}.')
        return choice

    def check_total(self, show=0):
        t = 0
        for i in self.cards:
            t += i.value
            if t > 21:
                if i.face == 'Ace':
                    t -= 10
        self.total = t

        if show:
            print(f'{self.name}\'s hand totals {self.total}.')
        return t


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
    tmp = [Player('Dealer', 0, 0)]
    n = howmanyplayers()
    # n = 1
    for i in range(1, n + 1):
        name = ''
        while not name:
            name = input(f'Enter player {i}\'s name: ')
        tmp.append(Player(name, i))
    return tmp


def deal(num):
    players[0].draw_card(1)      # Dealer draws one
    players[0].check_total()
    for p in range(1, num):
        players[p].draw_card(2)
        players[p].check_total()


# INITIAL SETUP
players = get_players()
deck = Deck()
deck.shuffle()
deal(len(players))

# PLAY GAME
game_on = True

while game_on:
    for p in players[1:]:
        move = 'hit'
        while move == 'hit':
            if p.number == 0:       # Dealer
                move = 'stand'
            else:
                players[0].view_cards()
                p.view_cards()
                move = p.choose_move()
                total = p.check_total()

            if move == 'hit':
                p.draw_card()
                total = p.check_total(0)
                if total > 21:
                    p.view_cards()
                    print(f'{p.name}\'s total is {p.total}')
                    print(F'BUST! {p.name} is out of the game!')
                    players.remove(p)
                    if len(players) == 1:       # Only Dealer remains
                        game_on = False
                        break
            elif move == 'stand':
                if total > players[0].total:
                    print(f'{p.name.upper()} HAS WON THE GAME!')
                    print('FINAL SCORE:')
                    print(f'  Dealer: {players[0].total}')
                    print(f'  {p.name}: {p.total}')
                    game_on = False
                    break
            break

