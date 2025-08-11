from fractions import Fraction

def solve():
    """Index: 7320.
    Returns: the number of gumballs remaining in the bowl.
    """
    # L1
    pedro_multiplier = 3 # three times the number Alicia has
    alicia_gumballs = 20 # Alicia has 20 gumballs
    pedro_additional_gumballs = pedro_multiplier * alicia_gumballs

    # L2
    pedro_total_gumballs = alicia_gumballs + pedro_additional_gumballs

    # L3
    total_gumballs_in_bowl = alicia_gumballs + pedro_total_gumballs

    # L4
    percentage_taken_out = Fraction(40, 100) # 40% of the gumballs
    gumballs_taken_out = percentage_taken_out * total_gumballs_in_bowl

    # L5
    gumballs_remaining = total_gumballs_in_bowl - gumballs_taken_out

    # FA
    answer = gumballs_remaining
    return answer