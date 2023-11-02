class AbstractAgent():
    def __init__(self, agent_name):
        ''' Initialize the agent's name (from either a string
        or an int) and hand (as an empty list). '''
        if isinstance(agent_name, int):
            self.name = self.get_agent_type_str() + str(agent_name)
        elif isinstance(agent_name, str):
            self.name = agent_name 
        else:
            raise TypeError(f"Unknown type for agent_name: {type(agent_name)}")

        self.hand = []

    def get_agent_type_str(self):
        ''' Name of the class. See __init__ in AbstractAgent for use. '''
        raise NotImplementedError('Either did not implement get_agent_type_str for Agent subclass,\n\tor trying to instantiate an AbstractAgent!')
    
    def get_legal_cards(self, led_suit_cards):
        '''
        Function to find the list of legal cards from the player's hand
        based on the list of cards in the suit of the card that was led.
        (Includes both jacks if the trump suit, and does not include
        the little jack in its non-trump suit. See game.euchre_hand.EuchreHand.initialize_suits.)

        return: list of cards (subset of hand) which are legal options to play.
        '''
        if led_suit_cards is None: 
            return self.hand 
        
        led_suit_cards_in_hand = set(led_suit_cards).intersection(self.hand)
        if len(led_suit_cards_in_hand) > 0:
            return list(led_suit_cards_in_hand)
        return self.hand 
    
    def choose_card(self, legal_cards, hand_state):
        ''' Function to choose a card which MUST be implemented in any subclass. '''
        raise NotImplementedError('Did not implement choose_card for Agent class!')
    
    def play_card(self, led_suit_cards, hand_state):
        ''' 
        Function to play a card by finding the list of valid cards,
        calling self.choose_card (implemented in each subclass), 
        and removing the card from the hand.
        
        return: 
            card (Card): the chosen card to be played.
        '''
        legal_cards = self.get_legal_cards(led_suit_cards)
        card = self.choose_card(legal_cards, hand_state)
        self.hand.remove(card)
        return card