import global_info as gl
import display as dsp 
from card import check_validity

class Player:
    def __init__(self, name, player_type='manual'):
        self.name = name
        self.hand = []
        self.type = player_type

    def get_valid_cards(self, led_suit_cards):
        if led_suit_cards is None: 
            return self.hand 
        
        led_suit_cards_in_hand = set(led_suit_cards).intersection(self.hand)
        if len(led_suit_cards_in_hand) > 0:
            return list(led_suit_cards_in_hand)
        return self.hand 

    def get_manual_card_choice(self, valid_cards):
        
        valid_cards_rep = dsp.get_hand_rep(valid_cards)
        card_str = input("Select a card by its number from [" + 
                         ", ".join([card_rep + f" ({i+1})" for i,card_rep in enumerate(valid_cards_rep)])
                         + "]: ")
        if card_str == "":
            return valid_cards[0]
        if card_str == "quit":
            raise gl.QuitGameException()
        if card_str not in [str(i+1) for i in range(len(valid_cards))]:
            print("Invalid card number! (Enter 'quit' to quit, or enter '' to choose the first valid card.)")
            return self.get_manual_card_choice(valid_cards)
        
        card_idx = int(card_str) - 1
        return valid_cards[card_idx]

    def play_card_manual(self, valid_cards, trump_suit, trick, display_trick=True):
        print("Your turn,", self.name, "!\nTrump suit is", trump_suit)
        if display_trick:
            print('Cards played:', dsp.get_hand_rep(trick))

        card = self.get_manual_card_choice(valid_cards)
        self.hand.remove(card)
        return card
    
    def play_card(self, led_suit_cards, hand_state, display_trick=False):
        trick,trump_suit = hand_state.trick, hand_state.trump_suit
        valid_cards = self.get_valid_cards(led_suit_cards)

        if self.type == 'manual':
            return self.play_card_manual(valid_cards, trump_suit, trick, display_trick)
        else:
            raise NotImplementedError(f'Player type {self.type} not yet implemented!')