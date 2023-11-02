from .abstract_agent import AbstractAgent

class BaselineAgent(AbstractAgent):
    ''' Deterministic baseline agent. Should play by a reasonable, but
    not too complicated, strategy. '''
    def choose_card(self, legal_cards, hand_state):
        ''' 
        Choose a card from the set of legal cards according to a simple, reasonable strategy.
        
        Strategy outline:
            If your PARTNER is WINNING, or you cannot beat the currently winning card,
                then play your worst card (tiebreak randomly if non-trump and non-lead-suit)
            Otherwise (i.e. if you CAN WIN but your PARTNER is NOT WINNIG),
                then play the worst card that will win you the trick (as of the currently cards on the table)
                
        return: card (Card): Choice of card to play.
        '''
        trump_suit, trick = hand_state.trump_suit, hand_state.trick
        raise NotImplementedError('Need to implement strategy for the deterministic baseline agent.')
    
    def get_agent_type_str(self):
        ''' Name of the class. See __init__ in AbstractAgent for use. '''
        return 'BaselineAgent'