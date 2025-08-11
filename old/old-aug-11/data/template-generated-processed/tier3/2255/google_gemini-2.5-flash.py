from fractions import Fraction

def solve():
    """Index: 2255.
    Returns: the number of kids who would receive 2 macarons each.
    """
    # L1
    mitch_macarons = 20 # Mitch made 20 macarons
    joshua_more_than_mitch = 6 # Joshua made 6 more macarons than Mitch
    joshua_macarons = mitch_macarons + joshua_more_than_mitch

    # L2
    miles_multiplier = 2 # half as many macarons as Miles
    miles_macarons = joshua_macarons * miles_multiplier

    # L3
    renz_fraction_numerator = 3 # 3/4 as many macarons as Miles
    renz_fraction_denominator = 4 # 3/4 as many macarons as Miles
    three_fourths_miles = miles_macarons * Fraction(renz_fraction_numerator, renz_fraction_denominator)

    # L4
    renz_fewer_than_fraction = 1 # 1 fewer than 3/4 as many macarons as Miles
    renz_macarons = three_fourths_miles - renz_fewer_than_fraction

    # L5
    total_macarons = mitch_macarons + joshua_macarons + miles_macarons + renz_macarons

    # L6
    macarons_per_kid = 2 # receive 2 macarons each
    num_kids = total_macarons / macarons_per_kid

    # FA
    answer = num_kids
    return answer