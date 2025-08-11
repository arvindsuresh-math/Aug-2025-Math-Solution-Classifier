from fractions import Fraction

def solve():
    """Index: 374.
    Returns: the total number of buyers who've visited the store in the three days.
    """
    # L1
    yesterday_fraction = Fraction(1, 2) # half the number of buyers
    day_before_buyers = 50 # the day before had 50 buyers
    yesterday_buyers = yesterday_fraction * day_before_buyers

    # L2
    today_increase = 40 # 40 more buyers
    today_buyers = today_increase + yesterday_buyers

    # L3
    total_buyers = today_buyers + yesterday_buyers + day_before_buyers

    # FA
    answer = total_buyers
    return answer