from fractions import Fraction

def solve():
    """Index: 4251.
    Returns: the number of miles Carly ran the week she was injured.
    """
    # L1
    initial_miles_week1 = 2 # running 2 miles a week
    twice_factor = 2 # twice as long
    extra_miles = 3 # plus 3 extra miles per week
    miles_week2 = initial_miles_week1 * twice_factor + extra_miles

    # L2
    fraction_week3 = Fraction(9, 7) # 9/7 as much as she ran the second week
    miles_week3 = fraction_week3 * miles_week2

    # L3
    reduction_miles = 5 # reduce her running time by 5 miles per week
    miles_injured_week = miles_week3 - reduction_miles

    # FA
    answer = miles_injured_week
    return answer