def solve():
    """Index: 5894.
    Returns: the total money the employee made.
    """
    # L1
    hourly_rate = 30 # 30 dollars an hour
    overtime_multiplier = 1.5 # additional 50%
    overtime_pay_per_hour = hourly_rate * overtime_multiplier

    # L2
    hours_first_3_days = 6 # 6 hours for the first 3 days
    remaining_days_multiplier = 2 # twice as many hours per day
    hours_per_day_remaining = hours_first_3_days * remaining_days_multiplier

    # L3
    total_hours_worked = hours_first_3_days + hours_first_3_days + hours_first_3_days + hours_per_day_remaining + hours_per_day_remaining

    # L4
    standard_workweek_hours = 40 # first 40 hours in the workweek
    overtime_hours = total_hours_worked - standard_workweek_hours

    # L5
    total_money_made = standard_workweek_hours * hourly_rate + overtime_hours * overtime_pay_per_hour

    # FA
    answer = total_money_made
    return answer