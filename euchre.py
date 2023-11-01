import random
import numpy as np # I use this only for an np.argmax call, 
# which in theory we could find another way to do or implement by hand with a few lines - DW


'''
Make Class for a Hand. Will play 5 tricks and return score. 
Potential to keep track of bidding history. 

Player class
Euchre Class
Hand class
Card_deck class. 

'''

from card_info import * 
import display as dsp

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def card_input_to_idx(self):
        # This should probably be a loop that goes until it receives satsifactory answer.
        hand_rep = dsp.get_hand_rep(self.hand)
        card_str = input("Select a card by its number from [" + 
                         ", ".join([card_rep + f" ({i+1})" for i,card_rep in enumerate(hand_rep)])
                         + "]: ")
        if card_str == "":
            return 0
        if card_str == "quit":
            raise QuitGameException()
        if card_str not in [str(i+1) for i in range(len(hand_rep))]:
            return -1
        
        return int(card_str) - 1

    def get_manual_card_choice(self):
        card_idx = self.card_input_to_idx()
        
        while card_idx == -1:
            print("Invalid card number! (Enter 'quit' to quit, or enter '' to choose the first card.)")
            card_idx = self.card_input_to_idx()

        return self.hand[card_idx]

    def play_card_manual(self, trump_suit, trick, display_trick=True):
        print("Trump suit is", trump_suit)
        if display_trick:
            print('Cards played:', dsp.get_hand_rep(trick))
            
        card = self.get_manual_card_choice()
        while not check_validity(trick, card, self.hand):
            print("Invalid card choice! Must follow suit!")
            card = self.get_manual_card_choice()

        self.hand.remove(card)
        return card
    
    def play_card(self, trump_suit, trick):
        raise NotImplementedError()

class Euchre:
    def __init__(self, player_names=None):
        self.player_names = player_names if player_names is not None else [str(i+1) for i in range(4)]
        self.players = [Player(name) for name in self.player_names]

        '''
        I think in general we can just use player indices (0-3)
        for most use cases in the code and then do self.players[player_idx]
        any time we need to acually access the player object.
         
        I also think we should maintain the convention that player[i+1] 
         sits to the left of player[i]. We can keep the same player indices
         across all hands, and just rotate dealer per hand. - DW
        '''
        self.dealer = 0 
        self.init_hand()

    def init_hand(self):
        self.initialize_deck()
        self.set_trump()

        self.set_dealer(self.dealer + 1) # Rotate dealer
        self.set_current_player(self.dealer + 1) # Left of dealer starts

        self.tricks_won = [0 for _ in range(N_PLAYERS)]
        self.deal_cards()

        # self.phase = 'Bidding' # Include separate bid/play phases in the same class? 
        # Or make different classes for EuchreBid and EuchrePlay ?

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def initialize_deck(self):
        self.deck = [Card(suit=suit, rank=rank) for suit in SUITS for rank in RANKS]
        self.shuffle_deck()

    def set_trump(self, suit=None):
        self.trump_suit = random.choice(SUITS) if suit is None else suit
    
    def set_dealer(self, player_idx):
        self.dealer = player_idx

    def set_current_player(self, player_idx: int):
        self.current_player_idx = player_idx
        self.current_player = self.players[self.current_player_idx]

    def increment_current_player(self):
        self.set_current_player((self.current_player_idx + 1) % N_PLAYERS)

    def get_current_player(self):
        return self.current_player_idx, self.current_player
    
    def get_players(self):
        return self.players

    def deal_cards(self):
        for _ in range(HAND_SIZE):
            for player in self.players:
                card = self.deck.pop()
                player.hand.append(card)

    def play_trick(self, display=False):
        trick = [None for _ in range(N_PLAYERS)]
        for _ in range(N_PLAYERS):
            if display: 
                dsp.display_trick(self.players, trick)

            player_idx,player = self.get_current_player()
            try:
                card_played = player.play_card_manual(self.trump_suit, trick, False) 

                # card_played = player.play_card(self.trump_suit, trick, self.hand_history)  
                # The last arg above will throw an error as implemented. We need to figure out 
                # what info needs to be passed to the player besides just the current trick
            except QuitGameException:
                print("Game was quit.")
                return

            assert check_validity(trick, card_played, player.hand)
            trick[player_idx] = card_played
            self.increment_current_player()

        if display: 
            dsp.display_trick(self.players, trick)
        self.tricks_won[np.argmax([self.card_value(card) for card in trick])] += 1

    def is_trump(self, card: Card):
        matching_suit = {
            'Spades': 'Clubs',
            'Hearts': 'Diamonds',
            'Clubs': 'Spades',
            'Diamonds': 'Hearts'
        }
        is_little_jack = card.rank == 'Jack' and card.suit == matching_suit[self.trump_suit]
        return card.suit == self.trump_suit or is_little_jack

    def card_value(self, card):
        # I'd argue that this, 
        # as well as maybe even is_trump (with a trump_suit arg added)
        # could go in the separate file card_info.py, 
        # possibly in a new class which just covers basic
        # card game logic, and then this class can be kept separate
        # to actually run the game and euchre-specific/trick-taking logic - DW

        # Note: This value assignment skips Jack = 2 for the trump suit,
        # but it should not matter since we only ever compare card values

        if not self.is_trump(card):
            # Non-trump cards get their normal value
            return RANKS.index(card.rank)
        
        if card.rank != 'Jack':
            # Trump non-jack cards get N_RANKS + their value (above all non-trumps)
            return N_RANKS + RANKS.index(card.rank)
        
        if card.suit == self.trump_suit:
            # If card is the big jack (above all trumps, and little jack)
            return 2 * N_RANKS + 1
        
        # IF card is the little jack (above all trumps, but not big jack)
        return 2 * N_RANKS 
    

if __name__ == '__main__':
    # Usage example:
    player_names = [f'Player {i}' for i in range(1,5)]
    game = Euchre(player_names=player_names)
    dsp.display_all_hands(game.get_players())

    # Play a trick
    game.play_trick(display=True)

    # # Determine the winner of the trick
    # print("Trick winner:", game.trick_winner[0].name)