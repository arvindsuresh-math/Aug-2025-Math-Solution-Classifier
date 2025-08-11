def solve():
    """Index: 1596.
    Returns: the total kilometers Nina would travel during 2 years.
    """
    # L1
    regular_distance = 400 # at least 400 kilometers
    twice_factor = 2 # twice that distance
    increased_distance = regular_distance * twice_factor

    # L2
    years_to_months = 24 # WK
    half_factor = 0.5 # WK
    months_half_period = years_to_months * half_factor

    # L3
    distance_regular_months = regular_distance * months_half_period

    # L4
    distance_increased_months = increased_distance * months_half_period

    # L5
    total_distance = distance_regular_months + distance_increased_months

    # FA
    answer = total_distance
    return answer