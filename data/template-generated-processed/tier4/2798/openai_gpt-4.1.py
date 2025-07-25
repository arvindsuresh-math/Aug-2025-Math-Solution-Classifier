def solve():
    """Index: 2798.
    Returns: the total amount John makes in a 30 day month.
    """
    # L1
    num_days_in_month = 30 # 30 day month
    work_interval = 2 # every other day
    work_days = num_days_in_month / work_interval

    # L2
    hours_per_day = 12 # 12 hours every other day
    total_hours = work_days * hours_per_day

    # L3
    former_hourly_wage = 20 # $20 an hour job
    raise_percent = 0.3 # 30% raise
    hourly_raise = former_hourly_wage * raise_percent

    # L4
    new_hourly_wage = former_hourly_wage + hourly_raise

    # L5
    total_earnings = new_hourly_wage * total_hours

    # FA
    answer = total_earnings
    return answer