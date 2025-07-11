def solve():
    """Index: 1394.
    Returns: the total number of birds Jen has.
    """
    # L4
    ducks = 150 # Jen has 150 ducks
    more_ducks_than_four_times_chickens = 10 # 10 more ducks
    multiplier_for_chickens = 4 # four times the number of chickens
    chickens = (ducks - more_ducks_than_four_times_chickens) / multiplier_for_chickens

    # L5
    total_birds = chickens + ducks

    # FA
    answer = total_birds
    return answer