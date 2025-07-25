def solve():
    """Index: 6052.
    Returns: the total number of birds Mr. Valentino has on the farm.
    """
    # L1
    num_chickens = 200 # 200 chickens
    multiplier_ducks_chickens = 2 # twice as many ducks as chickens
    num_ducks = multiplier_ducks_chickens * num_chickens

    # L2
    multiplier_turkeys_ducks = 3 # three times as many turkeys as ducks
    num_turkeys = multiplier_turkeys_ducks * num_ducks

    # L3
    total_ducks_turkeys = num_turkeys + num_ducks

    # L4
    total_birds = total_ducks_turkeys + num_chickens

    # FA
    answer = total_birds
    return answer