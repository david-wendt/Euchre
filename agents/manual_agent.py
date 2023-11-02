import random 

from game import global_info as gl
from game import display as dsp 
from game.card import check_validity
from .abstract_agent import AbstractAgent

class ManualAgent(AbstractAgent):
    ''' 
    "Agent" that prints trick status to the command line
    and asks for user input to choose which card to play.
    '''
    def get_agent_type_str(self):
        ''' Name of the class. See __init__ in AbstractAgent for use. '''
        return 'ManualAgent'

    def get_manual_card_choice(self, legal_cards):
        ''' 
        Get user input and parse it.
        
        Enter a valid number option to choose a card,
        or hit enter without a number to choose a random option,
        or enter "quit" to quit the game.
        '''
        legal_cards_rep = dsp.get_hand_rep(legal_cards)
        card_str = input("Select a card by its number from [" + 
                         ", ".join([card_rep + f" ({i+1})" for i,card_rep in enumerate(legal_cards_rep)])
                         + "]: ")
        if card_str == "":
            return random.choice(legal_cards)
        if card_str == "quit":
            raise gl.QuitGameException()
        if card_str not in [str(i+1) for i in range(len(legal_cards))]:
            print("Invalid card number! (Enter 'quit' to quit, or enter '' to choose a random valid card.)")
            return self.get_manual_card_choice(legal_cards)
        
        card_idx = int(card_str) - 1
        return legal_cards[card_idx]

    def choose_card(self, legal_cards, hand_state):
        ''' Function to choose from a list of valid cards. Called by play_card in AbstractAgent. '''
        trump_suit, trick = hand_state.trump_suit, hand_state.trick
        print("\nYour turn,", self.name, "!\nTrump suit is", trump_suit)
        dsp.display_trick(trick)
        return self.get_manual_card_choice(legal_cards)