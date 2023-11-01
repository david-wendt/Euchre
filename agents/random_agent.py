import random 
from .abstract_agent import AbstractAgent

class RandomAgent(AbstractAgent):
    def choose_card(self, valid_cards, hand_state):
        return random.choice(valid_cards)
    
    def get_agent_type_str(self):
        return 'RandomAgent'