from .global_info import * 

from collections import namedtuple

''' 
NamedTuple to represent a card. This format, rather than a class
(at least the way I [DW] tried implementing the class),
is necessary to compare two cards for equality. 
'''
Card = namedtuple('Card', ['suit', 'rank'])

# We can probably jsut delete this funciton, or comment it out, or move it somewhere else,
# and move Card to global_info.py
def check_validity(card, led_suit_cards, hand):
    print('DEPRECATION WARNING: check_validity should no longer be used for game functionality. Replaced by AbstractAgent.get_valid_cards.')
    if led_suit_cards is None: 
        return True

    if card in led_suit_cards:
        return True 

    for other_card in hand:
        if other_card in led_suit_cards:
            return False
        
    return True 