from . import global_info as gl

SUIT_SYMBOLS = {
    # White (non-filled) versions:
    # 'Hearts': '\u2661', 
    # 'Diamonds': '\u2662', 
    # 'Clubs': '\u2667', 
    # 'Spades': '\u2664'
    # ---------------------
    # Black (filled) versions:
    'Hearts': '\u2665', 
    'Diamonds': '\u2666', 
    'Clubs': '\u2663', 
    'Spades': '\u2660'
}

RANK_SYMBOLS = {rank: rank[0] if rank != '10' else rank for rank in gl.RANKS}

def get_card_rep(card):
    '''Returns the string representation for the card.'''
    if card is None: 
        return "[no card]"
    return RANK_SYMBOLS[card.rank] + SUIT_SYMBOLS[card.suit]

def get_hand_rep(hand):
    '''Returns a list of string representations for cards in the hand.'''
    return [get_card_rep(card) for card in hand]

def display_all_hands(players):
    '''Prints all hands.'''
    for player in players:
        print(player.name, get_hand_rep(player.hand))
    print()

def display_contract_status(contract_team, player_names):
    print(f'Team of {player_names[contract_team]} and {player_names[contract_team + 2]} won the contract.')

def display_hand_status(tricks_won, player_names):
    print(f"TRICKS WON: \n\t{player_names[0]} & {player_names[2]}: {tricks_won[0]}\n\t{player_names[1]} & {player_names[3]}: {tricks_won[1]}'")
    print()

def display_trick(trick, player_names=None, leader=None):
    assert len(trick) == gl.N_PLAYERS

    if player_names is None:
        trick_string = get_hand_rep(trick)
    else:
        assert len(player_names) == gl.N_PLAYERS
        trick_string = ', '.join([f'{player_names[i]}: {get_card_rep(trick[i])}' for i in range(gl.N_PLAYERS)])

    if leader is not None:
        if player_names is None:
            leader_string = 'P' + str(leader)
        else:
            leader_string = player_names[leader]
        trick_string += ', leader = ' + leader_string

    print('CARDS PLAYED:',trick_string)