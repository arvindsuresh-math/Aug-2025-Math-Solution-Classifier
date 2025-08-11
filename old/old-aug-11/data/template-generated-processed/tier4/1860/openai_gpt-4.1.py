def solve():
    """Index: 1860.
    Returns: the number of hours the movie theater operates each day.
    """
    # L1
    num_replays = 6 # being replayed 6 times
    movie_length_hours = 1.5 # movie that's 1.5 hours long
    total_movie_hours = num_replays * movie_length_hours

    # L2
    ad_length_minutes = 20 # 20-minute advertisement
    total_ad_minutes = ad_length_minutes * num_replays

    # L3
    minutes_per_hour = 60 # WK
    total_ad_hours = total_ad_minutes / minutes_per_hour

    # L4
    total_operating_hours = total_movie_hours + total_ad_hours

    # FA
    answer = total_operating_hours
    return answer