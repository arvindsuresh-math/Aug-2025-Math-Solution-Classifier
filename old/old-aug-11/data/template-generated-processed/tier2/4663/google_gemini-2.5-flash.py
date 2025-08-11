def solve():
    """Index: 4663.
    Returns: the total amount Mr. Deane will spend for his gas.
    """
    # L1
    cost_per_liter_today = 1.4 # cost per liter of gas is $1.4 today
    liters_today = 10 # fill his gas tank with 10 liters of gas today
    cost_today = cost_per_liter_today * liters_today

    # L2
    oil_price_rollback = 0.4 # $0.4 oil price rollback
    cost_per_liter_friday = cost_per_liter_today - oil_price_rollback

    # L3
    liters_friday = 25 # another 25 liters on Friday
    cost_friday = cost_per_liter_friday * liters_friday

    # L4
    total_cost = cost_today + cost_friday

    # FA
    answer = total_cost
    return answer