def solve():
    """Index: 854.
    Returns: the total number of minutes Jeff was able to run for that week.
    """
    # L1
    minutes_per_hour = 60 # WK
    num_days_mon_to_wed = 3 # Monday to Wednesday
    mon_to_wed_total = minutes_per_hour * num_days_mon_to_wed

    # L2
    thursday_short = 20 # cut short his run by 20 minutes
    thursday_minutes = minutes_per_hour - thursday_short

    # L3
    friday_extra = 10 # jog 10 minutes more on Friday
    friday_minutes = minutes_per_hour + friday_extra

    # L4
    total_minutes = mon_to_wed_total + thursday_minutes + friday_minutes

    # FA
    answer = total_minutes
    return answer