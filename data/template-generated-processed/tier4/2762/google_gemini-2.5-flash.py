def solve():
    """Index: 2762.
    Returns: the number of bottles of kombucha Henry can buy after receiving his cash refund.
    """
    # L1
    bottles_per_month = 15 # 15 bottles of kombucha every month
    months_per_year = 12 # WK
    total_bottles_per_year = bottles_per_month * months_per_year

    # L2
    refund_per_bottle = 0.10 # $0.10 per bottle
    total_refund_amount = refund_per_bottle * total_bottles_per_year

    # L3
    cost_per_bottle = 3.00 # Each bottle costs $3.00
    bottles_can_buy = total_refund_amount / cost_per_bottle

    # FA
    answer = bottles_can_buy
    return answer