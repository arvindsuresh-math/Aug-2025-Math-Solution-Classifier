def solve():
    """Index: 1955.
    Returns: the total money Ned makes a week.
    """
    # L1
    normal_mouse_cost = 120 # normal mice cost $120
    cost_increase_percent_decimal = 0.3 # 30% more
    cost_increase_amount = normal_mouse_cost * cost_increase_percent_decimal

    # L2
    left_handed_mouse_cost = normal_mouse_cost + cost_increase_amount

    # L3
    mice_sold_per_day = 25 # sells 25 a day
    daily_earnings = left_handed_mouse_cost * mice_sold_per_day

    # L4
    days_in_week = 7 # WK
    days_closed = 3 # except Sunday, Thursday, and Friday
    days_open_per_week = days_in_week - days_closed

    # L5
    weekly_earnings = daily_earnings * days_open_per_week

    # FA
    answer = weekly_earnings
    return answer