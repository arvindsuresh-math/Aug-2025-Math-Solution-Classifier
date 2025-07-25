def solve():
    """Index: 6982.
    Returns: the number of pounds of mangoes Kelly can buy.
    """
    # L1
    cost_per_half_pound = 0.60 # $0.60
    multiplier = 2 # WK
    cost_per_pound = cost_per_half_pound * multiplier

    # L2
    total_money = 12 # $12
    pounds_bought = total_money / cost_per_pound

    # FA
    answer = pounds_bought
    return answer