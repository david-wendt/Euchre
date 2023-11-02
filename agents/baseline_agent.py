from .abstract_agent import AbstractAgent

class BaselineAgent(AbstractAgent):
    ''' Deterministic baseline agent. Should play by a reasonable, but
    not too complicated, strategy. '''
    def choose_card(self, legal_cards, hand_state):
        raise NotImplementedError('Need to implement strategy for the deterministic baseline agent.')
    
    def get_agent_type_str(self):
        ''' Name of the class. See __init__ in AbstractAgent for use. '''
        return 'BaselineAgent'