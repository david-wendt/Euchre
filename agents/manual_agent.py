from game import global_info as gl
from game import display as dsp 
from game.card import check_validity
from .abstract_agent import AbstractAgent

class ManualAgent(AbstractAgent):
    def get_agent_type_str(self):
        return 'ManualAgent'

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

    def choose_card(self, valid_cards, hand_state):
        trump_suit, trick = hand_state.trump_suit, hand_state.trick
        print("Your turn,", self.name, "!\nTrump suit is", trump_suit)
        print('Cards played:', dsp.get_hand_rep(trick))
        return self.get_manual_card_choice(valid_cards)