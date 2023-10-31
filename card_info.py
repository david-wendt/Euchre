from collections import namedtuple

N_PLAYERS = 4
HAND_SIZE = 5
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['9', '10', 'Jack', 'Queen', 'King', 'Ace']
N_RANKS = len(RANKS)

Card = namedtuple('Card', ('suit', 'rank'))

class QuitGameException(Exception): pass 

def find_led_card(trick):
    prev_curr_pairs = [(trick[i-1],trick[i]) for i in range(len(trick))]
    for i in range(len(trick)):
        prev,curr = prev_curr_pairs[i]
        if prev is None and curr is not None:
            return curr
    raise Exception("Should never get here... Trick is as follows:" + str(trick))

def check_validity(trick, card_played, hand):
    led_card = find_led_card(trick)
    if card_played.suit == led_card.suit:
        return True 
    
    for other_card in hand:
        if other_card.suit == led_card.suit:
            return False
        
    return True 
