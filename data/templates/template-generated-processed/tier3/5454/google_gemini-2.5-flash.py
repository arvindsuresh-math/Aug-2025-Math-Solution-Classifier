from fractions import Fraction

def solve():
    """Index: 5454.
    Returns: the total number of stamps Maria wants to collect.
    """
    # L1
    initial_stamps = 40 # 40 stamps so far
    percentage_increase = Fraction(20, 100) # 20% more
    additional_stamps = initial_stamps * percentage_increase

    # L2
    total_stamps = initial_stamps + additional_stamps

    # FA
    answer = total_stamps
    return answer