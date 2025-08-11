def solve():
    """Index: 2200.
    Returns: the total number of legs among the animals Farmer Brown fed.
    """
    # L1
    num_chickens = 7 # 7 chickens
    legs_per_chicken = 2 # WK
    chicken_legs = num_chickens * legs_per_chicken

    # L2
    num_sheep = 5 # 5 sheep
    legs_per_sheep = 4 # WK
    sheep_legs = num_sheep * legs_per_sheep

    # L3
    total_legs = chicken_legs + sheep_legs

    # FA
    answer = total_legs
    return answer