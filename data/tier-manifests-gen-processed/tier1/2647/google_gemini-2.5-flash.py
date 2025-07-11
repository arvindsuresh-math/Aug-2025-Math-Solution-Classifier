def solve():
    """Index: 2647.
    Returns: the total number of rattlesnakes in the park.
    """
    # L1
    multiplier_pythons = 3 # three times as many pythons
    num_boa_constrictors = 40 # 40 boa constrictors
    num_pythons = multiplier_pythons * num_boa_constrictors

    # L2
    total_pythons_boa = num_pythons + num_boa_constrictors

    # L3
    total_snakes_in_park = 200 # 200 snakes in a park
    num_rattlesnakes = total_snakes_in_park - total_pythons_boa

    # FA
    answer = num_rattlesnakes
    return answer