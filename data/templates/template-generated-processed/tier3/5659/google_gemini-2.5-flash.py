from fractions import Fraction

def solve():
    """Index: 5659.
    Returns: the total number of visitors for the three months.
    """
    # L1
    october_visitors = 100 # 100 visitors in October
    increase_percentage = Fraction(15, 100) # increased by 15%
    november_increase = october_visitors * increase_percentage

    # L2
    november_visitors = october_visitors + november_increase

    # L3
    december_additional_visitors = 15 # 15 more visitors in December
    december_visitors = november_visitors + december_additional_visitors

    # L4
    total_visitors = october_visitors + november_visitors + december_visitors

    # FA
    answer = total_visitors
    return answer