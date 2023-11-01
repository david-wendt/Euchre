import game.global_info as gl 
from game.card import Card
from game.euchre import Euchre
from agents.manual_agent import ManualAgent

def test():
    card1 = Card('Spades', 'Jack')
    card2 = Card('Spades', 'Ace')
    card3 = Card('Spades', 'Jack')
    print(card1, card2, card3, card1 == card2, card1 == card3)

def main():
    players = [ManualAgent(f'Player {i}') for i in range(gl.N_PLAYERS)]
    game = Euchre(players, points_to_win=3, verbosity=2)
    game.play()

if __name__ == '__main__':
    # test()
    main()