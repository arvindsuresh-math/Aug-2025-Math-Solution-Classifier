from fractions import Fraction

def solve():
    """Index: 374.
    Returns: the total number of buyers who visited the store in the three days.
    """
    # L1
    day_before_yesterday_buyers = 50 # the day before had 50 buyers
    yesterday_fraction = Fraction(1, 2) # half the number of buyers yesterday as there were the day before
    yesterday_buyers = yesterday_fraction * day_before_yesterday_buyers

    # L2
    buyers_difference = 40 # 40 more buyers in the grocery store today than yesterday
    today_buyers = buyers_difference + yesterday_buyers

    # L3
    total_buyers = today_buyers + yesterday_buyers + day_before_yesterday_buyers

    # FA
    answer = total_buyers
    return answer