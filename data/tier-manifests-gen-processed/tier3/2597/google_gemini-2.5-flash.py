from fractions import Fraction

def solve():
    """Index: 2597.
    Returns: the total number of rehabilitation centers visited by all.
    """
    # L1
    lisa_visits = 6 # If Lisa visited 6 rehabilitation centers
    half_fraction = Fraction(1, 2) # half fewer rehabilitation centers
    jude_visits = half_fraction * lisa_visits

    # L2
    twice_multiplier = 2 # twice as many rehabilitation centers
    less_than_amount = 2 # 2 less than
    han_visits = twice_multiplier * jude_visits - less_than_amount

    # L3
    more_than_amount = 6 # 6 more than
    jane_twice_multiplier = 2 # twice as many rehabilitation centers as Han
    jane_visits = more_than_amount + jane_twice_multiplier * han_visits

    # L4
    total_visits = lisa_visits + jude_visits + han_visits + jane_visits

    # FA
    answer = total_visits
    return answer