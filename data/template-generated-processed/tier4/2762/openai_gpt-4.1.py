def solve():
    """Index: 2762.
    Returns: the number of bottles Henry can buy after receiving his cash refund for a year.
    """
    # L1
    bottles_per_month = 15 # Henry drinks 15 bottles of kombucha every month
    months_per_year = 12 # there are 12 months in 1 year
    total_bottles = bottles_per_month * months_per_year

    # L2
    refund_per_bottle = 0.10 # cash refund of $0.10 per bottle
    total_refund = refund_per_bottle * total_bottles

    # L3
    bottle_cost = 3.00 # each bottle costs $3.00
    bottles_can_buy = total_refund / bottle_cost

    # FA
    answer = bottles_can_buy
    return answer