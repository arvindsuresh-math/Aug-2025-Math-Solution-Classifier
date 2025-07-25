def solve():
    """Index: 7444.
    Returns: the total number of minutes Mark played.
    """
    # L1
    num_weeks = 2 # for 2 weeks
    days_in_week = 7 # WK
    total_gigs = days_in_week * num_weeks

    # L2
    short_song_length = 5 # 5 minutes long
    long_song_multiplier = 2 # twice that long
    long_song_length = short_song_length * long_song_multiplier

    # L3
    minutes_per_gig = short_song_length + short_song_length + long_song_length

    # L4
    total_minutes_played = total_gigs * minutes_per_gig

    # FA
    answer = total_minutes_played
    return answer