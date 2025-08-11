def solve():
    """Index: 2157.
    Returns: the difference between Collete's and Rachel's age.
    """
    # L1
    rona_age = 8 # Rona is 8 years old
    rachel_multiplier = 2 # twice as old as Rona
    rachel_age = rona_age * rachel_multiplier

    # L2
    collete_divisor = 2 # half the age of Rona's
    collete_age = rona_age / collete_divisor

    # L3
    age_difference = rachel_age - collete_age

    # FA
    answer = age_difference
    return answer