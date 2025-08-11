from fractions import Fraction

def solve():
    """Index: 6730.
    Returns: the number of carrots not used that day.
    """
    # L1
    initial_carrots = 300 # 300 carrots in a bucket
    used_before_lunch_fraction = Fraction(2, 5) # used 2/5 of the carrots
    carrots_used_before_lunch = used_before_lunch_fraction * initial_carrots

    # L2
    remaining_carrots_after_lunch = initial_carrots - carrots_used_before_lunch

    # L3
    used_end_of_day_fraction = Fraction(3, 5) # used 3/5 of the remaining carrots
    carrots_used_end_of_day = used_end_of_day_fraction * remaining_carrots_after_lunch

    # L4
    carrots_not_used = remaining_carrots_after_lunch - carrots_used_end_of_day

    # FA
    answer = carrots_not_used
    return answer