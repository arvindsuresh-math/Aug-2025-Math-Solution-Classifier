def solve():
    """Index: 1807.
    Returns: the number of Monster Club cards Oliver has.
    """
    # L1
    battle_gremlins_cards = 48 # His Battle Gremlins card collection is the largest at 48 cards
    times_larger_than_alien_baseball = 3 # three times the size of his Alien Baseball card collection
    alien_baseball_cards = battle_gremlins_cards / times_larger_than_alien_baseball

    # L2
    monster_club_multiplier = 2 # twice as many Monster Club cards
    monster_club_cards = alien_baseball_cards * monster_club_multiplier

    # FA
    answer = monster_club_cards
    return answer