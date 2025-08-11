from fractions import Fraction

def solve():
    """Index: 1958.
    Returns: the total number of minutes Rickey took to finish the race.
    """
    # L6
    total_time_both = 70 # took a total of 70 minutes
    prejean_speed_fraction_numerator = 3 # three-quarters that of Rickey
    prejean_speed_fraction_denominator = 4 # three-quarters that of Rickey
    one_whole = 1 # WK
    combined_coefficient_numerator = one_whole * prejean_speed_fraction_denominator + prejean_speed_fraction_numerator
    combined_coefficient_denominator = prejean_speed_fraction_denominator
    reciprocal_numerator = combined_coefficient_denominator
    reciprocal_denominator = combined_coefficient_numerator
    rickey_time = total_time_both * Fraction(reciprocal_numerator, reciprocal_denominator)

    # FA
    answer = rickey_time
    return answer