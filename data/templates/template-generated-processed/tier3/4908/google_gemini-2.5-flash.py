from fractions import Fraction

def solve():
    """Index: 4908.
    Returns: the total number of jeans both of Noah's closets can fit.
    """
    # L1
    ali_closet_capacity = 200 # Ali's closet, which can fit 200 pairs of jeans
    fraction_capacity = Fraction(1, 4) # 1/4 as much as Ali's closet
    noah_single_closet_capacity = ali_closet_capacity * fraction_capacity

    # L2
    num_noah_closets = 2 # two closets
    total_noah_closet_capacity = noah_single_closet_capacity * num_noah_closets

    # FA
    answer = total_noah_closet_capacity
    return answer