from fractions import Fraction

def solve():
    """Index: 302.
    Returns: the total square feet of wrapping paper Carrie needs for all three presents.
    """
    # L1
    first_present = 2 # One present needs two square feet
    second_present_fraction_numerator = 3 # three-quarters of that amount
    second_present_fraction_denominator = 4 # three-quarters of that amount
    second_present = Fraction(second_present_fraction_numerator, second_present_fraction_denominator) * first_present

    # L2
    third_present = first_present + second_present

    # L3
    total_wrapping_paper = first_present + second_present + third_present

    # FA
    answer = total_wrapping_paper
    return answer