def solve():
    """Index: 7240.
    Returns: the number of weeks until chickens are cheaper than buying eggs.
    """
    # L1
    num_chickens = 4 # 4 chickens
    cost_per_chicken = 20 # $20 each
    initial_chicken_cost = num_chickens * cost_per_chicken

    # L2
    eggs_per_chicken_per_week = 3 # each produces 3 eggs a week
    eggs_produced_per_week = num_chickens * eggs_per_chicken_per_week

    # L3
    cost_per_dozen_bought = 2 # spent $2 per dozen
    chicken_feed_cost_per_week = 1 # $1 in total a week to feed
    weekly_savings = cost_per_dozen_bought - chicken_feed_cost_per_week

    # L4
    weeks_to_pay_off_chickens = initial_chicken_cost / weekly_savings

    # L5
    offset_for_first_profit_week = 1 # WK
    weeks_until_cheaper = weeks_to_pay_off_chickens + offset_for_first_profit_week

    # FA
    answer = weeks_until_cheaper
    return answer