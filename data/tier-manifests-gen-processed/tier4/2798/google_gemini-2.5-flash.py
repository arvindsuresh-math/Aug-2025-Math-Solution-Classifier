def solve():
    """Index: 2798.
    Returns: the total amount John makes in a 30 day month.
    """
    # L1
    total_days_in_month = 30 # 30 day month
    work_frequency_divisor = 2 # every other day
    work_days_in_month = total_days_in_month / work_frequency_divisor

    # L2
    hours_per_work_day = 12 # 12 hours every other day
    total_hours_in_month = work_days_in_month * hours_per_work_day

    # L3
    former_hourly_rate = 20 # $20 an hour job
    raise_percentage = 0.3 # 30% raise
    hourly_raise_amount = former_hourly_rate * raise_percentage

    # L4
    new_hourly_rate = former_hourly_rate + hourly_raise_amount

    # L5
    total_earnings = new_hourly_rate * total_hours_in_month

    # FA
    answer = total_earnings
    return answer