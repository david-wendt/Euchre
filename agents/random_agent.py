import random 
from .abstract_agent import AbstractAgent

class RandomAgent(AbstractAgent):
    ''' Agent that randomly chooses a card from the list of valid card choices. '''
    
    def choose_card(self, legal_cards, hand_state):
        ''' Randomly chose a card. Called by play_card in AbstractAgent. '''
        return random.choice(legal_cards)
    
    def get_agent_type_str(self):
        ''' Name of the class. See __init__ in AbstractAgent for use. '''
        return 'RandomAgent'