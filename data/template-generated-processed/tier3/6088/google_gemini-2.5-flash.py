def solve():
    """Index: 6088.
    Returns: the number of shirts Kim has left.
    """
    # L1
    num_dozens = 4 # 4 dozen shirts
    shirts_per_dozen = 12 # WK
    initial_shirts = num_dozens * shirts_per_dozen

    # L2
    fraction_given_away_denominator = 3 # 1/3 of them
    shirts_given_away = initial_shirts / fraction_given_away_denominator

    # L3
    shirts_left = initial_shirts - shirts_given_away

    # FA
    answer = shirts_left
    return answer