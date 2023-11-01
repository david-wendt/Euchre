import random

from . import global_info as gl
from .bidding import Bidding
from .euchre_hand import EuchreHand

class Euchre:
    def __init__(self, players, dealer=0, points_to_win=gl.POINTS_TO_WIN, verbosity=0):
        self.players = players 
        self.player_names = [player.name for player in self.players]
        assert len(self.players) == gl.N_PLAYERS
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
                # TODO: send this print stuff to display?
                print(f'{self.player_names[hand_winning_team]} & {self.player_names[hand_winning_team + 2]} win the hand!')
                print(f'They won {points} points!')
                print(f'Current Score:\n\t{self.player_names[0]} & {self.player_names[2]}: {self.team_points[0]}\n\t{self.player_names[1]} & {self.player_names[3]}: {self.team_points[1]}')
                print()

        winning_team = max(range(gl.N_TEAMS), key=lambda i: self.team_points[i])

        if self.verbosity:
            print(f'Congratulations! Players {self.player_names[winning_team]} & {self.player_names[winning_team + 2]} win!')
            print(f'Final Score:\n\t{self.player_names[0]} & {self.player_names[2]}: {self.team_points[0]}\n\t{self.player_names[1]} & {self.player_names[3]}: {self.team_points[1]}')
            print()
        
        return winning_team