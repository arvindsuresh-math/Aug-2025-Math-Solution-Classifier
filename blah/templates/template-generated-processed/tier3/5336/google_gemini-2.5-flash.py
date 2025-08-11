def solve():
    """Index: 5336.
    Returns: the number of loops Tammy should make per day.
    """
    # L1
    total_meters_per_week = 3500 # 3500 meters per week
    track_length_meters = 50 # 50 meters around
    total_laps_per_week = total_meters_per_week / track_length_meters

    # L2
    days_in_week = 7 # WK
    laps_per_day = total_laps_per_week / days_in_week

    # FA
    answer = laps_per_day
    return answer