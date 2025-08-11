from fractions import Fraction

def solve():
    """Index: 2648.
    Returns: the age difference between Halima and Beckham.
    """
    # L1
    halima_ratio_part = 4 # The ratio representing the age of Halima, Beckham, and Michelle is 4:3:7
    beckham_ratio_part = 3 # The ratio representing the age of Halima, Beckham, and Michelle is 4:3:7
    michelle_ratio_part = 7 # The ratio representing the age of Halima, Beckham, and Michelle is 4:3:7
    total_ratio_parts = halima_ratio_part + beckham_ratio_part + michelle_ratio_part

    # L2
    total_age = 126 # the total age for the three siblings is 126
    halima_fraction = Fraction(halima_ratio_part, total_ratio_parts)
    halima_age = halima_fraction * total_age

    # L3
    beckham_fraction = Fraction(beckham_ratio_part, total_ratio_parts)
    beckham_age = beckham_fraction * total_age

    # L4
    age_difference = halima_age - beckham_age

    # FA
    answer = age_difference
    return answer