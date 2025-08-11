def solve():
    """Index: 3306.
    Returns: the total hours Larry jogs for two weeks.
    """
    # L1
    days_week_1 = 3 # jogs for 3 days
    days_week_2 = 5 # jogs for 5 days
    total_days_jogged = days_week_1 + days_week_2

    # L2
    minutes_per_day = 30 # jogs for 30 minutes each day
    total_minutes_jogged = total_days_jogged * minutes_per_day

    # L3
    minutes_per_hour = 60 # WK
    total_hours_jogged = total_minutes_jogged / minutes_per_hour

    # FA
    answer = total_hours_jogged
    return answer