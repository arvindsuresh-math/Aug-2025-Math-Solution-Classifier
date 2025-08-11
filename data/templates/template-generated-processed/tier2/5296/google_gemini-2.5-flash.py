def solve():
    """Index: 5296.
    Returns: the total profit Bob makes a week.
    """
    # L1
    muffins_per_dozen = 12 # a dozen muffins
    cost_per_muffin_buy = 0.75 # $0.75 each
    daily_buy_cost = muffins_per_dozen * cost_per_muffin_buy

    # L2
    sell_price_per_muffin = 1.5 # $1.5 each
    daily_sell_revenue = muffins_per_dozen * sell_price_per_muffin

    # L3
    daily_profit = daily_sell_revenue - daily_buy_cost

    # L4
    days_per_week = 7 # WK
    weekly_profit = daily_profit * days_per_week

    # FA
    answer = weekly_profit
    return answer