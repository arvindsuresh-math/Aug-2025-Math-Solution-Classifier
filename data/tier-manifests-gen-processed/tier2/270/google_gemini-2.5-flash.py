def solve():
    """Index: 270.
    Returns: the total phone bill at the end of the month.
    """
    # L2
    minutes_per_hour = 60 # WK
    cost_per_minute = 0.05 # five cents per minute
    cost_per_call = minutes_per_hour * cost_per_minute

    # L3
    customers_per_week = 50 # 50 customers a week
    weekly_bill = customers_per_week * cost_per_call

    # L4
    weeks_per_month = 4 # WK
    monthly_bill = weekly_bill * weeks_per_month

    # FA
    answer = monthly_bill
    return answer