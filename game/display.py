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

def display_trick(players, trick, tricks_won, contract_team, display_hands=True):
    '''Prints all hands (optional) along with cards played in this trick.'''
    for player_idx,player in enumerate(players):
        print(player.name)
        if display_hands:
            print("\tHAND:", get_hand_rep(player.hand))
        print("\tCARD PLAYED:", get_card_rep(trick[player_idx]))
    
    print(f'Team of Players {contract_team} and {contract_team + 2} won the contract.')
    print(f"TRICKS WON: Players 0 and 2: {tricks_won[0]}, Players 1 and 3: {tricks_won[1]}'")
    print()