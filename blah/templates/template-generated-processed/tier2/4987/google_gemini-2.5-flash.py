def solve():
    """Index: 4987.
    Returns: how much more expensive 5 bottles of wine will be in 2 months.
    """
    # L1
    num_bottles = 5 # 5 bottles of wine
    cost_per_bottle_today = 20.00 # $20.00 today
    total_cost_today = num_bottles * cost_per_bottle_today

    # L2
    tariff_increase_percent_num = 25 # increase by 25%
    tariff_increase_percent_decimal = 0.25 # .25*100
    increase_cost = tariff_increase_percent_decimal * total_cost_today

    # FA
    answer = increase_cost
    return answer