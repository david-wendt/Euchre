from collections import namedtuple
import random
import numpy as np # I use this only for an np.argmax call, 
# which in theory we could find another way to do or implement by hand with a few lines - DW


N_PLAYERS = 4
HAND_SIZE = 5
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['9', '10', 'Jack', 'Queen', 'King', 'Ace']
N_RANKS = len(RANKS)
Card = namedtuple('Card', ('suit', 'rank'))

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, trump_suit, trick):
        raise NotImplementedError()
        return card

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
        self.set_current_player(self.current_player_idx + 1)

    def get_current_player(self):
        return self.current_player_idx, self.current_player

    def deal_cards(self):
        for _ in range(HAND_SIZE):
            for player in self.players:
                card = self.deck.pop()
                player.hand.append(card)

    def check_validity(self, trick, card_played):
        raise NotImplementedError()

    def play_trick(self):
        trick = [None for _ in range(N_PLAYERS)]
        for _ in range(N_PLAYERS):
            player_idx,player = self.get_current_player()
            card_played = player.play_card(self.trump_suit, trick, 
                                                 self.hand_history) 
                # This line will throw an error as implemented. We need to figure out 
                # what info needs to be passed to the player besides just the current trick

            assert self.check_validity(trick, card_played)
            trick[player_idx] = card_played
            self.increment_current_player()
        self.tricks_won[np.argmax([self.card_value(card) for card in trick])] += 1

    def is_trump(self, card: Card):
        matching_suit = {
            'Spades': 'Clubs',
            'Hearts': 'Diamonds',
            'Clubs': 'Spades',
            'Diamonds': 'Hearts'
        }
        is_little_jack = card.rank = 'Jack' and card.suit == matching_suit[self.trump_suit]
        return card.suit == self.trump_suit or is_little_jack

    def card_value(self, card):
        # I'd argue that this, and the constants I defined above,
        # as well as maybe even is_trump (with a trump_suit arg added)
        # could go in a separate file/class which just covers basic
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
    
    def display(self):
        for player in self.players:
            print(player.name, player.hand)


if __name__ == '__main__':
    # Usage example:
    player_names = [f'Player {i}' for i in range(1,5)]
    game = Euchre(player_names=player_names)
    game.display()

    # # Play a trick
    # game.play_trick()

    # # Determine the winner of the trick
    # print("Trick winner:", game.trick_winner[0].name)