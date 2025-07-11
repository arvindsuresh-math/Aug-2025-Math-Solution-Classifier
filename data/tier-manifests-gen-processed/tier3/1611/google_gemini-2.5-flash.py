from fractions import Fraction

def solve():
    """Index: 1611.
    Returns: the total number of miles traveled for 3 days.
    """
    # L1
    first_day_miles = 200 # On the first day, they traveled 200 miles
    second_day_fraction = Fraction(3, 4) # On the second day, they traveled 3/4 as far
    second_day_miles = first_day_miles * second_day_fraction

    # L2
    first_two_days_total = first_day_miles + second_day_miles

    # L3
    third_day_fraction = Fraction(1, 2) # On the third day, they traveled 1/2 as many miles as the first two days combined
    third_day_miles = first_two_days_total * third_day_fraction

    # L4
    total_miles_3_days = first_day_miles + second_day_miles + third_day_miles

    # FA
    answer = total_miles_3_days
    return answer