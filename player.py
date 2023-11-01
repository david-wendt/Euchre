import global_info as gl
import display as dsp 
from card import check_validity

class Player:

    '''
    TODO: Adapt this to take a player_type (or something like that), with 
    options like 'manual', 'RL_model_1', 'RL_model_2', ...
    and then automatically switch between possible play_card functions
    based on the player_type
    '''

    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_manual_card_choice(self, card_checker):
        
        hand_rep = dsp.get_hand_rep(self.hand)
        card_str = input("Select a card by its number from [" + 
                         ", ".join([card_rep + f" ({i+1})" for i,card_rep in enumerate(hand_rep)])
                         + "]: ")
        if card_str == "":
            card_idx = 0
            while not card_checker(card_idx):
                card_idx += 1
            return card_idx
        if card_str == "quit":
            raise gl.QuitGameException()
        if card_str not in [str(i+1) for i in range(len(hand_rep))]:
            print("Invalid card number! (Enter 'quit' to quit, or enter '' to choose the first valid card.)")
            return self.get_manual_card_choice(card_checker)
        
        card_idx = int(card_str) - 1
        if not card_checker(card_idx):
            print("Invalid card choice! Must follow suit!")
            return self.get_manual_card_choice(card_checker)
    
        return card_idx

    def play_card_manual(self, led_suit_cards, trump_suit, trick, display_trick=True):
        print("Your turn,", self.name, "!\nTrump suit is", trump_suit)
        if display_trick:
            print('Cards played:', dsp.get_hand_rep(trick))

        def card_checker(card_idx):
            return check_validity(self.hand[card_idx], led_suit_cards, self.hand)
            
        card_idx = self.get_manual_card_choice(card_checker)
        card = self.hand[card_idx]
        self.hand.remove(card)
        return card
    
    def play_card(self, trump_suit, trick):
        raise NotImplementedError()