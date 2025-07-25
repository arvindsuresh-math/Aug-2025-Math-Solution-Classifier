def solve():
    """Index: 3099.
    Returns: the total number of hours Natasha and Esteban exercised.
    """
    # L1
    natasha_daily_minutes = 30 # exercised for 30 minutes every day
    days_in_week = 7 # for one week
    natasha_total_minutes = natasha_daily_minutes * days_in_week

    # L2
    esteban_daily_minutes = 10 # exercised for 10 minutes
    esteban_days = 9 # on each of nine days
    esteban_total_minutes = esteban_daily_minutes * esteban_days

    # L3
    total_minutes = natasha_total_minutes + esteban_total_minutes

    # L4
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer