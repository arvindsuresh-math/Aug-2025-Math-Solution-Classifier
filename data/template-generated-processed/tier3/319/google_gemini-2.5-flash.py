from fractions import Fraction

def solve():
    """Index: 319.
    Returns: the number of diaries Natalie's sister has now.
    """
    # L1
    initial_diaries = 8 # 8 small diaries
    double_factor = 2 # double the number of diaries
    diaries_bought = double_factor * initial_diaries

    # L2
    total_diaries_after_purchase = diaries_bought + initial_diaries

    # L3
    lost_fraction = Fraction(1, 4) # lost 1/4 of what she had
    diaries_lost = lost_fraction * total_diaries_after_purchase

    # L4
    remaining_diaries = total_diaries_after_purchase - diaries_lost

    # FA
    answer = remaining_diaries
    return answer