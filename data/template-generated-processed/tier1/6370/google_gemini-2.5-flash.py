def solve():
    """Index: 6370.
    Returns: the total amount the car's owner had to pay.
    """
    # L1
    hours_per_day = 8 # He works 8 hours a day
    num_days_worked = 14 # for 14 days
    total_hours_worked = hours_per_day * num_days_worked

    # L2
    hourly_rate = 60 # $60 an hour
    labor_cost = hourly_rate * total_hours_worked

    # L3
    parts_cost = 2500 # $2500 in parts
    total_cost = labor_cost + parts_cost

    # FA
    answer = total_cost
    return answer