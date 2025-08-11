def solve():
    """Index: 3086.
    Returns: the total amount the company will pay all 50 new employees.
    """
    # L1
    num_reps = 50 # hire 50 new phone reps
    hours_per_day = 8 # work 8 hours a day
    total_daily_hours = num_reps * hours_per_day

    # L2
    num_days = 5 # After 5 days
    total_hours_over_period = num_days * total_daily_hours

    # L3
    hourly_wage = 14.00 # paid $14.00 an hour
    total_cost = hourly_wage * total_hours_over_period

    # FA
    answer = total_cost
    return answer