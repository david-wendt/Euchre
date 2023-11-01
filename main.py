import game.global_info as gl 
from game.card import Card
from game.euchre import Euchre
from agents.manual_agent import ManualAgent
from agents.random_agent import RandomAgent

def test():
    pass 

def main():
    # players = [ManualAgent(f'Player {i}') for i in range(gl.N_PLAYERS)]
    players = [RandomAgent(i) for i in range(gl.N_PLAYERS - 1)]
    players.append(ManualAgent('David'))
    game = Euchre(players, points_to_win=3, verbosity=2)
    game.play()

if __name__ == '__main__':
    # test()
    main()