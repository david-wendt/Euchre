'''
Define some necessary global constants for the game 
which are the same across all games and hands.
'''

N_PLAYERS = 4
N_TEAMS = 2
HAND_SIZE = 5
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
RANKS = ['9', '10', 'Jack', 'Queen', 'King', 'Ace']
N_RANKS = len(RANKS)
MATCHING_SUITS = {
    'Spades': 'Clubs',
    'Hearts': 'Diamonds',
    'Clubs': 'Spades',
    'Diamonds': 'Hearts'
}

TEAM_OF_PLAYER = {
    0: 0,
    1: 1,
    2: 0,
    3: 1
} # I know this is just mod 2, but I think it helps readability

POINTS_TO_WIN = 10

class QuitGameException(Exception): 
    ''' Exception used to quit early when playing manually from the command line. '''
    def __init__(self):            
        # Call the base class constructor with the parameters it needs
        super().__init__('Game was quit!')
