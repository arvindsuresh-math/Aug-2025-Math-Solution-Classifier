def solve():
    """Index: 1394.
    Returns: the total number of birds Jen has.
    """
    # L2
    ducks = 150 # Jen has 150 ducks
    duck_chicken_offset = 10 # 10 more ducks than four times the number of chickens
    chicken_multiplier = 4 # four times the number of chickens
    # ducks = duck_chicken_offset + chicken_multiplier * chickens
    # Rearranged: chickens = (ducks - duck_chicken_offset) // chicken_multiplier
    chickens = (ducks - duck_chicken_offset) // chicken_multiplier

    # L5
    total_birds = chickens + ducks

    # FA
    answer = total_birds
    return answer