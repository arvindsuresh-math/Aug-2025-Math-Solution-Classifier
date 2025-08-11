def solve():
    """Index: 7269.
    Returns: the total money paid to the magician.
    """
    # L1
    weeks_worked = 2 # 2 weeks
    days_per_week = 7 # WK
    total_days_worked = weeks_worked * days_per_week

    # L2
    hours_per_day = 3 # 3 hours every day
    total_hours_worked = total_days_worked * hours_per_day

    # L3
    hourly_rate = 60 # $60 an hour
    total_payment = total_hours_worked * hourly_rate

    # FA
    answer = total_payment
    return answer