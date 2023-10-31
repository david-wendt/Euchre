from collections import namedtuple

N_PLAYERS = 4
HAND_SIZE = 5
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['9', '10', 'Jack', 'Queen', 'King', 'Ace']
N_RANKS = len(RANKS)

Card = namedtuple('Card', ('suit', 'rank'))