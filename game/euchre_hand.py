import random 
from collections import namedtuple

from . import global_info as gl
from . import display as dsp
from .card import Card

def robust_index(ls: list, elt):
    ''' 
    Utility function used for determining trick winner.
    
    Identical to Python's native list.index(), but returns -1
    upon not finding the element instead of throwing a ValueError.
    '''
    try: 
        return ls.index(elt)
    except ValueError:
        return -1

''' NamedTuple for state of the hand to include the cards played in the trick and the trump suit. '''
HandState = namedtuple('HandState', ('trick', 'trump_suit'))

class EuchreHand():
    ''' 
    Class to run a hand of Euchre.
    
    Stores references to all players, stores the state of the hand and the
    state of each trick within the hand, and can loop through tricks
    and evaluate who won the hand and how many points they win.
    '''
    def __init__(self, players, dealer, bidding_winner, trump_suit, 
                 bidding_history=None, verbosity=0):
        self.players = players 
        self.player_names = [player.name for player in self.players]
        self.leading_player = (dealer + 1) % gl.N_PLAYERS
        self.contract_team = gl.TEAM_OF_PLAYER[bidding_winner]
        self.trump_suit = trump_suit
        self.tricks_won = [0 for _ in range(gl.N_TEAMS)]
        self.verbosity = verbosity 

        self.initialize_suits()
        self.initialize_deck()
        self.deal_cards()

    def initialize_deck(self):
        ''' Set up the deck and shuffle it. '''
        self.deck = [Card(suit=suit, rank=rank) for suit in gl.SUITS for rank in gl.RANKS]
        random.shuffle(self.deck)

    def initialize_suits(self):
        '''
        Set up the suits for the hand. Copy the default suits, then move both 
        Jacks to the trump suit and make sure the order of cards within each suit is correct
        (including in the trump suit with the two Jacks).
        '''
        print('WARNING: This suit-card-list computation should probably be cached once ahead of time instead of computed once per hand...')
        suit_cards = {suit: [Card(suit, rank) for rank in gl.RANKS] for suit in gl.SUITS}
        trump_suit = self.trump_suit
        other_suit = gl.MATCHING_SUITS[self.trump_suit]
        suit_cards[trump_suit].remove(Card(trump_suit, 'Jack'))
        suit_cards[other_suit].remove(Card(other_suit, 'Jack'))
        suit_cards[trump_suit].append(Card(other_suit, 'Jack'))
        suit_cards[trump_suit].append(Card(trump_suit, 'Jack'))
        self.suit_cards = suit_cards

    def deal_cards(self):
        ''' Deal out cards to the players. '''
        for _ in range(gl.HAND_SIZE):
            for player in self.players:
                card = self.deck.pop()
                player.hand.append(card)
        # TODO: Maybe sort the cards by suit in each player's hand?
        # Or perhaps do that in display.py when get_hand_rep is called?

    def play_trick(self, verbosity):
        ''' 
        Play a single trick, looping through players to receive
        card choices, and then determine the winner. 

        return: 
            winner (int): player index (0-3) of the winner of the trick
        '''
        trick = [None for _ in range(gl.N_PLAYERS)]
        player_idx = self.leading_player
        led_suit_cards = None 

        if verbosity:
            dsp.display_contract_status(self.contract_team, self.player_names)

        for i in range(gl.N_PLAYERS):
            player_idx = (self.leading_player + i) % gl.N_PLAYERS
            player = self.players[player_idx]

            if verbosity > 2: 
                dsp.display_all_hands(self.players)

            hand_state = HandState(trump_suit=self.trump_suit, trick=trick) # TODO: Make this a class? 
            card_played = player.play_card(led_suit_cards, hand_state) 

            if player_idx == self.leading_player:
                # Extra jack logic here to prevent needing to search through the suit lists every trick
                if card_played.rank != 'Jack':
                    led_suit_cards = self.suit_cards[card_played.suit]
                elif card_played.suit in [self.trump_suit, gl.MATCHING_SUITS[self.trump_suit]]:
                    led_suit_cards = self.suit_cards[self.trump_suit]
                else:
                    led_suit_cards = self.suit_cards[card_played.suit]

            trick[player_idx] = card_played

        winning_suit_cards = led_suit_cards
        if len(set(trick).intersection(self.suit_cards[self.trump_suit])) > 0:
            # A trump was played
            winning_suit_cards = self.suit_cards[self.trump_suit]

        winner = max(range(gl.N_PLAYERS), key=lambda i: robust_index(winning_suit_cards, trick[i]))
        self.tricks_won[gl.TEAM_OF_PLAYER[winner]] += 1

        if verbosity: 
            dsp.display_trick(trick, player_names=self.player_names, leader=self.leading_player)
            print(f'{self.player_names[winner]} won with {dsp.get_card_rep(trick[winner])}!\n')
            dsp.display_tricks_won(self.tricks_won, self.player_names)

        for player_idx in range(gl.N_PLAYERS):
            if gl.TEAM_OF_PLAYER[player_idx] == gl.TEAM_OF_PLAYER[winner]:
                self.players[player_idx].reward(1) # Reward 1 if your team wins the trick
            else:
                self.players[player_idx].reward(-1) # Reward -1 if your team loses the trick

        return winner

    def play_hand(self):
        '''
        Main function to play a hand and loop through five tricks.

        return: 
            winning_team (int): index (0 or 1) of the winning team
            points (int): number of points won by th ewinning team
        '''
        for _ in range(gl.HAND_SIZE):
            self.leading_player = self.play_trick(self.verbosity)

        winning_team = max(range(gl.N_TEAMS), key=lambda i: self.tricks_won[i])

        if winning_team == self.contract_team:
            if self.tricks_won[winning_team] == 5:
                # Contract-winning team sweeps
                points = 2
            else:
                # Contract-winning team wins but doesn't sweep
                points = 1
        else:
            # Non-contract team wins
            points = 2

        for player_idx in range(gl.N_PLAYERS):
            if gl.TEAM_OF_PLAYER[player_idx] == winning_team:
                self.players[player_idx].reward(10*points) # Reward 10*points if your team wins the hand

        return winning_team, points 