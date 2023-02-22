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

    def __str__(self):
        return f'Player #{self.number}: \'{self.name}\''


players = []
