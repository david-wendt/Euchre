import random 
from collections import namedtuple

from . import global_info as gl
from . import display as dsp
from .card import Card, check_validity

def robust_index(ls: list, elt):
    # Used for determining trick winner
    try: 
        return ls.index(elt)
    except ValueError:
        return -1

HandState = namedtuple('HandState', ('trick', 'trump_suit'))

class EuchreHand():
    def __init__(self, players, dealer, bidding_winner, trump_suit, 
                 bidding_history=None, verbosity=0):
        self.players = players 
        self.leading_player = (dealer + 1) % gl.N_PLAYERS
        self.contract_team = gl.TEAM_OF_PLAYER[bidding_winner]
        self.trump_suit = trump_suit
        self.tricks_won = [0 for _ in range(gl.N_TEAMS)]
        self.verbosity = verbosity 

        self.initialize_suits()
        self.initialize_deck()
        self.deal_cards()

    def initialize_deck(self):
        self.deck = [Card(suit=suit, rank=rank) for suit in gl.SUITS for rank in gl.RANKS]
        random.shuffle(self.deck)

    def initialize_suits(self):
        # The cards should be in rank order for all suits, including trump.
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
        for _ in range(gl.HAND_SIZE):
            for player in self.players:
                card = self.deck.pop()
                player.hand.append(card)

    def play_trick(self, verbosity):
        trick = [None for _ in range(gl.N_PLAYERS)]
        player_idx = self.leading_player
        led_suit_cards = None 
        for i in range(gl.N_PLAYERS):
            player_idx = (self.leading_player + i) % gl.N_PLAYERS
            player = self.players[player_idx]

            if verbosity: 
                dsp.display_trick(self.players, trick, self.tricks_won, self.contract_team)

            hand_state = HandState(trump_suit=self.trump_suit, trick=trick) # TODO: Make this a class? 
            card_played = player.play_card(led_suit_cards, hand_state) 

            assert check_validity(card_played, led_suit_cards, player.hand)

            if player_idx == self.leading_player:
                led_suit_cards = self.suit_cards[card_played.suit]

            trick[player_idx] = card_played

        winning_suit_cards = led_suit_cards
        if len(set(trick).intersection(self.suit_cards[self.trump_suit])) > 0:
            # A trump was played
            winning_suit_cards = self.suit_cards[self.trump_suit]

        winner = max(range(gl.N_PLAYERS), key=lambda i: robust_index(winning_suit_cards, trick[i]))
        self.tricks_won[gl.TEAM_OF_PLAYER[winner]] += 1

        if verbosity: 
            dsp.display_trick(self.players, trick, self.tricks_won, self.contract_team)
            print(f'Player {winner} won with {dsp.get_card_rep(trick[winner])}!\n')

        return winner

    def play_hand(self):
        for _ in range(5):
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

        return winning_team, points 