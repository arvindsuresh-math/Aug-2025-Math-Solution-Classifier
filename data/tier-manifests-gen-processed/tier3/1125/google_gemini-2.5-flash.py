from fractions import Fraction

def solve():
    """Index: 1125.
    Returns: the total number of kitchen supplies Sharon wants to buy.
    """
    # L1
    pots_angela = 20 # 20 pots
    plates_multiplier_angela = 3 # three times as many plates
    plates_more_than_three_times_angela = 6 # 6 more than three times as many plates
    plates_angela = plates_more_than_three_times_angela + plates_multiplier_angela * pots_angela

    # L2
    cutlery_fraction_angela = Fraction(1, 2) # half as many cutlery
    cutlery_angela = cutlery_fraction_angela * plates_angela

    # L3
    pots_sharon_fraction = Fraction(1, 2) # half as many pots as Angela
    pots_sharon = pots_sharon_fraction * pots_angela

    # L4
    plates_sharon_multiplier = 3 # three times as many plates as Angela
    plates_sharon_less = 20 # 20 less than three times as many plates as Angela
    plates_sharon = plates_sharon_multiplier * plates_angela - plates_sharon_less

    # L5
    cutlery_sharon_multiplier = 2 # twice as much cutlery as Angela
    cutlery_sharon = cutlery_sharon_multiplier * cutlery_angela

    # L6
    total_supplies_sharon = pots_sharon + plates_sharon + cutlery_sharon

    # FA
    answer = total_supplies_sharon
    return answer