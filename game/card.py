from .global_info import * 

from collections import namedtuple

# This is necessary in order to compare cards and handle lists of cards
Card = namedtuple('Card', ['suit', 'rank'])

def check_validity(card, led_suit_cards, hand):
    print('WARNING: check_validity should not be necessary for game functionality and should only be used for double-checking.')
    if led_suit_cards is None: 
        return True

    if card in led_suit_cards:
        return True 

    for other_card in hand:
        if other_card in led_suit_cards:
            return False
        
    return True 