def solve():
    """Index: 1860.
    Returns: the total hours the movie theater operates each day.
    """
    # L1
    movie_length_hours = 1.5 # 1.5 hours long
    num_replays = 6 # replayed 6 times
    total_movie_time_hours = movie_length_hours * num_replays

    # L2
    ad_duration_minutes = 20 # 20-minute advertisement
    total_ad_time_minutes = ad_duration_minutes * num_replays

    # L3
    minutes_per_hour = 60 # WK
    total_ad_time_hours = total_ad_time_minutes / minutes_per_hour

    # L4
    total_operation_hours = total_movie_time_hours + total_ad_time_hours

    # FA
    answer = total_operation_hours
    return answer