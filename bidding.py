import random 
import global_info as gl 

class Bidding():
    def run_bidding(self):
        print('WARNING: Bidding has not yet been implemented, so just returning a random player and suit for now.')
        return random.choice(range(gl.N_PLAYERS)), random.choice(gl.SUITS)
        