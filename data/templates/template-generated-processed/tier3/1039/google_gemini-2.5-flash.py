from fractions import Fraction

def solve():
    """Index: 1039.
    Returns: the number of apartments with only one resident.
    """
    # L1
    at_least_one_percent = Fraction(85, 100) # 85% of them have at least 1 resident
    total_apartments = 120 # 120 apartments
    apartments_with_at_least_one = at_least_one_percent * total_apartments

    # L2
    at_least_two_percent = Fraction(60, 100) # 60% of the apartments have at least two residents
    apartments_with_at_least_two = at_least_two_percent * total_apartments

    # L3
    intermediate_difference = apartments_with_at_least_one - apartments_with_at_least_two
    one_multiplier = 1 # WK
    apartments_with_only_one = intermediate_difference * one_multiplier

    # FA
    answer = apartments_with_only_one
    return answer