def solve():
    """Index: 7194.
    Returns: the combined distance for three of them for the whole week.
    """
    # L1
    julien_daily_distance = 50 # Julien swam 50 meters
    days_in_week = 7 # WK
    julien_weekly_distance = julien_daily_distance * days_in_week

    # L2
    sarah_multiplier = 2 # swims twice the distance
    sarah_daily_distance = sarah_multiplier * julien_daily_distance

    # L3
    sarah_weekly_distance = sarah_daily_distance * days_in_week

    # L4
    jamir_extra_distance = 20 # Jamir swims 20 more meters per day than Sarah
    jamir_daily_distance = sarah_daily_distance + jamir_extra_distance

    # L5
    jamir_weekly_distance = jamir_daily_distance * days_in_week

    # L6
    combined_weekly_distance = jamir_weekly_distance + sarah_weekly_distance + julien_weekly_distance

    # FA
    answer = combined_weekly_distance
    return answer