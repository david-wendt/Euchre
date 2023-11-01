class AbstractAgent():
    def __init__(self, agent_name):
        if isinstance(agent_name, int):
            self.name = self.get_agent_type_str() + str(agent_name)
        elif isinstance(agent_name, str):
            self.name = agent_name 
        else:
            raise TypeError(f"Unknown type for agent_name: {type(agent_name)}")

        self.hand = []

    def get_agent_type_str(self):
        raise NotImplementedError('Either did not implement get_agent_type_str for Agent subclass,\n\tor trying to instantiate an AbstractAgent!')
    
    def get_valid_cards(self, led_suit_cards):
        if led_suit_cards is None: 
            return self.hand 
        
        led_suit_cards_in_hand = set(led_suit_cards).intersection(self.hand)
        if len(led_suit_cards_in_hand) > 0:
            return list(led_suit_cards_in_hand)
        return self.hand 
    
    def choose_card(self, valid_cards, hand_state):
        raise NotImplementedError('Did not implement choose_card for Agent class!')
    
    def play_card(self, led_suit_cards, hand_state):
        valid_cards = self.get_valid_cards(led_suit_cards)
        card = self.choose_card(valid_cards, hand_state)
        self.hand.remove(card)
        return card