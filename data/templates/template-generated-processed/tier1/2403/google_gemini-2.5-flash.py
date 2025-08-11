def solve():
    """Index: 2403.
    Returns: the total distance the two friends bike in a week.
    """
    # L1
    onur_daily_distance = 250 # 250 kilometers a day
    days_biking_per_week = 5 # Five times a week
    onur_weekly_distance = days_biking_per_week * onur_daily_distance

    # L2
    hanil_extra_daily_distance = 40 # 40 more kilometers
    hanil_daily_distance = onur_daily_distance + hanil_extra_daily_distance

    # L3
    hanil_weekly_distance = hanil_daily_distance * days_biking_per_week

    # L4
    total_weekly_distance = hanil_weekly_distance + onur_weekly_distance

    # FA
    answer = total_weekly_distance
    return answer