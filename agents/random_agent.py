import random 

class RandomAgent():
    def __init__(self):
        pass 

    def play_card(self, valid_cards):
        return random.choice(valid_cards)