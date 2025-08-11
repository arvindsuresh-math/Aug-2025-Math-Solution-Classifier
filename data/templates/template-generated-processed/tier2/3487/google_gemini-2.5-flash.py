def solve():
    """Index: 3487.
    Returns: the total amount Johnny spends on crab meat in a week.
    """
    # L1
    dishes_per_day = 40 # 40 times a day
    crab_meat_per_dish = 1.5 # 1.5 pounds of crab meat
    daily_crab_meat_pounds = dishes_per_day * crab_meat_per_dish

    # L2
    cost_per_pound = 8 # $8 per pound
    daily_cost = daily_crab_meat_pounds * cost_per_pound

    # L3
    days_in_week = 7 # WK
    closed_days_per_week = 3 # closed 3 days a week
    open_days_per_week = days_in_week - closed_days_per_week

    # L4
    weekly_cost = daily_cost * open_days_per_week

    # FA
    answer = weekly_cost
    return answer