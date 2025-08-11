def solve():
    """Index: 2647.
    Returns: the total number of rattlesnakes in the park.
    """
    # L1
    pythons_per_boa = 3 # three times as many pythons as boa constrictors
    boa_constrictors = 40 # 40 boa constrictors
    pythons = pythons_per_boa * boa_constrictors

    # L2
    pythons_and_boa = pythons + boa_constrictors

    # L3
    total_snakes = 200 # 200 snakes in a park
    rattlesnakes = total_snakes - pythons_and_boa

    # FA
    answer = rattlesnakes
    return answer