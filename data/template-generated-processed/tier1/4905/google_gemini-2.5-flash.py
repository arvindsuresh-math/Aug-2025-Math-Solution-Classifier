def solve():
    """Index: 4905.
    Returns: the number of regular toenails Hilary can fit into the remainder of the jar.
    """
    # L1
    big_toenails_filled = 20 # 20 big toenails
    big_toe_size_multiplier = 2 # twice as big as the rest
    space_taken_by_big_toenails_in_regular_units = big_toenails_filled * big_toe_size_multiplier

    # L2
    regular_toenails_filled = 40 # 40 regular toenails
    total_space_filled_in_regular_units = regular_toenails_filled + space_taken_by_big_toenails_in_regular_units

    # L3
    jar_capacity_regular_toenails = 100 # 100 toenails in the jar
    remaining_capacity_regular_toenails = jar_capacity_regular_toenails - total_space_filled_in_regular_units

    # FA
    answer = remaining_capacity_regular_toenails
    return answer