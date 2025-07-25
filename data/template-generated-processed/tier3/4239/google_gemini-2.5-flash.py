def solve():
    """Index: 4239.
    Returns: the number of packs of buns Alex needed to buy.
    """
    # L1
    invited_friends = 10 # invited 10 friends
    friends_not_eating_meat = 1 # 1 of his friends didn't eat meat
    friends_to_cook_for = invited_friends - friends_not_eating_meat

    # L2
    burgers_per_guest = 3 # cook 3 burgers for each guest
    total_burgers_needed = burgers_per_guest * friends_to_cook_for

    # L3
    friends_not_eating_bread = 1 # Another one of his friends didn't eat bread
    buns_needed_after_adjustment = total_burgers_needed - burgers_per_guest

    # L4
    buns_per_pack = 8 # The burger buns came 8 to a pack
    packs_of_buns_needed = buns_needed_after_adjustment / buns_per_pack

    # FA
    answer = packs_of_buns_needed
    return answer