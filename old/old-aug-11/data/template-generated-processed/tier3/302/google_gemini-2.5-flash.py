from fractions import Fraction

def solve():
    """Index: 302.
    Returns: the total square feet of wrapping paper Carrie needs.
    """
    # L1
    first_present_paper = 2 # One present needs two square feet of wrapping paper
    second_present_fraction = Fraction(3, 4) # three-quarters of that amount
    second_present_paper = second_present_fraction * first_present_paper

    # L2
    third_present_paper = first_present_paper + second_present_paper

    # L3
    total_paper = first_present_paper + second_present_paper + third_present_paper

    # FA
    answer = total_paper
    return answer