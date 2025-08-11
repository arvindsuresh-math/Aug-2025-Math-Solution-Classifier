from fractions import Fraction

def solve():
    """Index: 5599.
    Returns: the total distance Mairead has covered.
    """
    # L1
    ran_miles = 40 # runs for 40 miles
    jogged_fraction = Fraction(3, 5) # 3/5 times as many miles as she ran
    jogged_miles = jogged_fraction * ran_miles

    # L2
    running_jogging_total = jogged_miles + ran_miles

    # L3
    walked_multiplier = 5 # walks for five times the number of miles she jogged
    walked_miles = walked_multiplier * jogged_miles

    # L4
    total_distance = walked_miles + running_jogging_total

    # FA
    answer = total_distance
    return answer