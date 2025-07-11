def solve():
    """Index: 270.
    Returns: the phone bill at the end of the month.
    """
    # L2
    minutes_per_hour = 60 # An hour has 60 minutes.
    cost_per_minute = 0.05 # each phone call is charged five cents per minute
    cost_per_customer = minutes_per_hour * cost_per_minute

    # L3
    customers_per_week = 50 # talk to 50 customers a week
    weekly_cost = customers_per_week * cost_per_customer

    # L4
    weeks_per_month = 4 # In a month of 4 weeks
    monthly_cost = weekly_cost * weeks_per_month

    # FA
    answer = monthly_cost
    return answer