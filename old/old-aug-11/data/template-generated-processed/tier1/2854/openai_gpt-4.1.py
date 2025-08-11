def solve():
    """Index: 2854.
    Returns: the total number of minutes Javier and Sanda exercised together.
    """
    # L1
    javier_minutes_per_day = 50 # Javier exercised for 50 minutes every day
    days_in_week = 7 # one week
    javier_total = javier_minutes_per_day * days_in_week

    # L2
    sanda_minutes_per_day = 90 # Sanda exercised for 90 minutes
    sanda_days = 3 # on each of three days
    sanda_total = sanda_minutes_per_day * sanda_days

    # L3
    total_minutes = javier_total + sanda_total

    # FA
    answer = total_minutes
    return answer