def solve():
    """Index: 1040.
    Returns: the difference in number between goats and pigs.
    """
    # L1
    goats = 66 # 66 goats at a farm
    chicken_multiplier = 2 # twice as many chickens
    chickens = goats * chicken_multiplier

    # L2
    total_goats_chickens = goats + chickens

    # L3
    duck_divisor = 2 # half of the total of the goats and chickens
    ducks = total_goats_chickens / duck_divisor

    # L4
    pig_divisor = 3 # a third of the number of ducks
    pigs = ducks / pig_divisor

    # L5
    difference_goats_pigs = goats - pigs

    # FA
    answer = difference_goats_pigs
    return answer