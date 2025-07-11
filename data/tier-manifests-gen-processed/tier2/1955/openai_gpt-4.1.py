def solve():
    """Index: 1955.
    Returns: the amount of money Ned makes in a week from selling left-handed mice.
    """
    # L1
    normal_mouse_cost = 120 # normal mice cost $120
    price_increase_percent = 0.3 # cost 30% more
    price_increase = normal_mouse_cost * price_increase_percent

    # L2
    left_mouse_cost = normal_mouse_cost + price_increase

    # L3
    mice_sold_per_day = 25 # sells 25 a day
    daily_revenue = left_mouse_cost * mice_sold_per_day

    # L4
    days_in_week = 7 # WK
    closed_days = 3 # open every day except Sunday, Thursday, and Friday
    open_days = days_in_week - closed_days

    # L5
    weekly_revenue = daily_revenue * open_days

    # FA
    answer = weekly_revenue
    return answer