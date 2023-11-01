from .abstract_agent import AbstractAgent

class BaselineAgent(AbstractAgent):
    def choose_card(self, valid_cards, hand_state):
        raise NotImplementedError('Need to implement strategy for the deterministic baseline agent.')
    
    def get_agent_type_str(self):
        return 'BaselineAgent'