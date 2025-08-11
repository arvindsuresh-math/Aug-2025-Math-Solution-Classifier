def solve():
    """Index: 2881.
    Returns: the difference in the number of tadpoles and fish remaining in the pond.
    """
    # L1
    initial_fish = 50 # 50 fish in a pond
    tadpole_multiplier = 3 # 3 times as many tadpoles
    initial_tadpoles = initial_fish * tadpole_multiplier

    # L2
    caught_fish = 7 # catches 7 fish
    remaining_fish = initial_fish - caught_fish

    # L3
    tadpole_development_divisor = 2 # half the tadpoles develop into frogs
    remaining_tadpoles = initial_tadpoles / tadpole_development_divisor

    # L4
    difference_tadpoles_fish = remaining_tadpoles - remaining_fish

    # FA
    answer = difference_tadpoles_fish
    return answer