from fractions import Fraction

def solve():
    """Index: 772.
    Returns: the total number of apples Kylie picked.
    """
    # L1
    apples_first_hour = 66 # The first hour she picks 66 apples

    # L2
    doubling_factor = 2 # doubles her apple picking rate
    apples_second_hour = apples_first_hour * doubling_factor

    # L3
    fraction_third_hour_numerator = 1 # a third of the apples
    fraction_third_hour_denominator = 3 # a third of the apples
    fraction_third_hour = Fraction(fraction_third_hour_numerator, fraction_third_hour_denominator)
    apples_third_hour = apples_first_hour * fraction_third_hour

    # L4
    total_apples = apples_first_hour + apples_second_hour + apples_third_hour

    # FA
    answer = total_apples
    return answer