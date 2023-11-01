import game.global_info as gl 
from game.card import Card
from game.euchre import Euchre

def test():
    card1 = Card('Spades', 'Jack')
    card2 = Card('Spades', 'Ace')
    card3 = Card('Spades', 'Jack')
    print(card1, card2, card3, card1 == card2, card1 == card3)

def main():
    player_names = [f'Player {i}' for i in range(gl.N_PLAYERS)]
    player_types = [f'manual' for i in range(gl.N_PLAYERS)]
    game = Euchre(player_names, player_types, points_to_win=3, verbosity=2)
    game.play()

if __name__ == '__main__':
    # test()
    main()