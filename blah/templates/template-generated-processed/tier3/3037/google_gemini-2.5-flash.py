from fractions import Fraction

def solve():
    """Index: 3037.
    Returns: the number of visitors who did not fall ill.
    """
    # L1
    total_visitors = 500 # 500 visitors
    ill_percentage = Fraction(40, 100) # 40 percent of the aquarium visitors fell ill
    visitors_fell_ill = ill_percentage * total_visitors

    # L2
    visitors_not_ill = total_visitors - visitors_fell_ill

    # FA
    answer = visitors_not_ill
    return answer