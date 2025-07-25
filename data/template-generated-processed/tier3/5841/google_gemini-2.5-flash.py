from fractions import Fraction

def solve():
    """Index: 5841.
    Returns: the difference in amount Moses gets compared to Esther.
    """
    # L1
    moses_percentage = Fraction(40, 100) # 40% of the total amount
    total_amount = 50 # share $50
    moses_share = moses_percentage * total_amount

    # L2
    remainder = total_amount - moses_share

    # L3
    num_people_splitting = 2 # Tony and Esther will split the remainder equally among themselves
    tony_esther_share = remainder / num_people_splitting

    # L4
    difference = moses_share - tony_esther_share

    # FA
    answer = difference
    return answer