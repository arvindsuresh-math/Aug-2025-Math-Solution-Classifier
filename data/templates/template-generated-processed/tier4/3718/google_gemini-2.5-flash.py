def solve():
    """Index: 3718.
    Returns: the number of days it will take to make back the money.
    """
    # L1
    initial_cost = 100000 # $100,000 to open initially
    daily_cost_percent = 0.01 # 1% of that to run per day
    daily_running_cost = initial_cost * daily_cost_percent

    # L2
    tickets_per_day = 150 # 150 tickets a day
    price_per_ticket = 10 # $10 each
    daily_revenue = tickets_per_day * price_per_ticket

    # L3
    daily_profit = daily_revenue - daily_running_cost

    # L4
    days_to_break_even = initial_cost / daily_profit

    # FA
    answer = days_to_break_even
    return answer