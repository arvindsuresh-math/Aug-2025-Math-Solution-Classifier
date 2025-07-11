def solve():
    """Index: 915.
    Returns: Allyn's total monthly expenses on electricity in June.
    """
    # L1
    bulb_watt_per_day = 60 # each bulb uses 60 watts of power each day
    num_bulbs = 40 # 40 such bulbs in his house
    total_watt_per_day = bulb_watt_per_day * num_bulbs

    # L2
    june_days = 30 # June, with 30 days
    total_watt_june = june_days * total_watt_per_day

    # L3
    cost_per_watt = 0.20 # twenty cents per power watt used
    total_cost = total_watt_june * cost_per_watt

    # FA
    answer = total_cost
    return answer