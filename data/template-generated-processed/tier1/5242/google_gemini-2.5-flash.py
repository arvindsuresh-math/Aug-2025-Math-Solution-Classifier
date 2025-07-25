def solve():
    """Index: 5242.
    Returns: the total number of stuffed animals Willy has.
    """
    # L1
    initial_stuffed_animals = 10 # Willy has 10 stuffed animals
    mom_gives = 2 # mom gives him 2 more stuffed animals
    after_mom_gives = initial_stuffed_animals + mom_gives

    # L2
    dad_multiplier = 3 # 3 times more stuffed animals
    dad_gives = after_mom_gives * dad_multiplier

    # L3
    total_stuffed_animals = after_mom_gives + dad_gives

    # FA
    answer = total_stuffed_animals
    return answer