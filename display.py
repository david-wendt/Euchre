from card_info import * 

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

RANK_SYMBOLS = {rank: rank[0] if rank != '10' else rank for rank in RANKS}

def display_card(card):
    if card is None: 
        return "[no card]"
    return RANK_SYMBOLS[card.rank] + SUIT_SYMBOLS[card.suit]

def display_hand(hand):
    return [display_card(card) for card in hand]

def display_all_hands(players):
    for player in players:
        print(player.name, display_hand(player.hand))
    print()

def display_trick(players, trick, display_hands=True):
    for player_idx,player in enumerate(players):
        print(player.name)
        if display_hands:
            print("\tHAND:", display_hand(player.hand))
        print("\tCARD PLAYED:", display_card(trick[player_idx]))
    print()