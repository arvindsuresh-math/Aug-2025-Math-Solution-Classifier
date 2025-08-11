def solve():
    """Index: 4337.
    Returns: the profit Carrie earned on the cake.
    """
    # L1
    hours_per_day = 2 # 2 hours a day
    num_days_worked = 4 # for 4 days
    total_hours_worked = hours_per_day * num_days_worked

    # L2
    hourly_rate = 22 # $22 an hour
    total_wages = hourly_rate * total_hours_worked

    # L3
    cost_of_supplies = 54 # cost for supplies to make the cake was $54
    profit = total_wages - cost_of_supplies

    # FA
    answer = profit
    return answer