def solve():
    """Index: 6701.
    Returns: the total amount of sleep Prudence gets in 4 weeks.
    """
    # L1
    nights_sleep_6_hours = 5 # From Sunday to Thursday, Prudence sleeps 6 hours a night.
    hours_sleep_weekday = 6 # sleeps 6 hours a night
    hours_from_weekday_sleep = nights_sleep_6_hours * hours_sleep_weekday

    # L2
    nights_sleep_9_hours = 2 # Friday and Saturday she sleeps for 9 hours a night.
    hours_sleep_weekend_night = 9 # sleeps for 9 hours a night
    hours_from_weekend_night_sleep = nights_sleep_9_hours * hours_sleep_weekend_night

    # L3
    days_nap = 2 # on Saturday and Sunday
    hours_nap_per_day = 1 # a 1-hour nap
    hours_from_nap = days_nap * hours_nap_per_day

    # L4
    total_sleep_per_week = hours_from_weekday_sleep + hours_from_weekend_night_sleep + hours_from_nap

    # L5
    num_weeks = 4 # in 4 weeks
    total_sleep_4_weeks = num_weeks * total_sleep_per_week

    # FA
    answer = total_sleep_4_weeks
    return answer