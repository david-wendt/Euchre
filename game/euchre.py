import random

from . import global_info as gl
from . import display as dsp
from .player import Player 
from .bidding import Bidding
from .euchre_hand import EuchreHand

class Euchre:
    def __init__(self, player_names=None, player_types=None, dealer=0, 
                 points_to_win=gl.POINTS_TO_WIN, verbosity=0):
        self.player_names = player_names if player_names is not None else ['P'+str(i) for i in range(gl.N_PLAYERS)]
        self.player_types = player_types if player_types is not None else ['manual' for i in range(gl.N_PLAYERS)]
        assert len(self.player_names) == gl.N_PLAYERS
        assert len(self.player_types) == gl.N_PLAYERS
        self.players = [Player(self.player_names[i], self.player_types[i]) for i in range(gl.N_PLAYERS)]

        self.dealer = dealer
        self.points_to_win = points_to_win
        self.team_points = [0 for _ in range(gl.N_TEAMS)]
        self.verbosity = verbosity

    def play(self):
        while max(self.team_points) < self.points_to_win:
            bidding_winner,trump_suit = Bidding().run_bidding()
            hand = EuchreHand(self.players, self.dealer, bidding_winner, trump_suit, verbosity=self.verbosity)
            hand_winning_team,points = hand.play_hand()
            self.team_points[hand_winning_team] += points


            if self.verbosity > 1:
                print(f'Players {hand_winning_team} and {hand_winning_team + 2} win the hand!')
                print(f'They won {points} points!')
                print(f'Current Score:\n\tPlayers 0 and 2: {self.team_points[0]}\n\tPlayers 1 and 3: {self.team_points[1]}')
                print()

        winning_team = max(range(gl.N_TEAMS), key=lambda i: self.team_points[i])

        if self.verbosity:
            print(f'Congratulations! Players {winning_team} and {winning_team + 2} win!')
            print(f'Final Score:\n\tPlayers 0 and 2: {self.team_points[0]}\n\tPlayers 1 and 3: {self.team_points[1]}')
            print()
        
        return winning_team