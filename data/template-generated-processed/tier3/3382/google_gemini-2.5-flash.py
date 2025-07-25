def solve():
    """Index: 3382.
    Returns: the number of additional vacation days Andrew can still take.
    """
    # L1
    days_worked_total = 300 # Andrew worked 300 days
    days_to_earn_one_vacation_day = 10 # for every 10 days worked, you get 1 vacation day
    earned_vacation_days = days_worked_total / days_to_earn_one_vacation_day

    # L2
    march_vacation_days = 5 # took 5 days off in March
    september_multiplier = 2 # twice as many in September
    september_vacation_days = march_vacation_days * september_multiplier

    # L3
    total_vacation_days_used = march_vacation_days + september_vacation_days

    # L4
    remaining_vacation_days = earned_vacation_days - total_vacation_days_used

    # FA
    answer = remaining_vacation_days
    return answer