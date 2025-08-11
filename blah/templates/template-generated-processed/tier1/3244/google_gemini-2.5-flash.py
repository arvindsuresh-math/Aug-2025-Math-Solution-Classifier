def solve():
    """Index: 3244.
    Returns: the total time the show plays songs in minutes.
    """
    # L1
    show_duration_hours = 3 # 3 hours a day
    minutes_per_hour = 60 # WK
    total_show_minutes = show_duration_hours * minutes_per_hour

    # L2
    num_talking_segments = 3 # 3 talking segments
    talking_segment_duration = 10 # 10 minutes each
    total_talking_minutes = num_talking_segments * talking_segment_duration

    # L3
    num_ad_breaks = 5 # 5 ad breaks
    ad_break_duration = 5 # 5 minutes each
    total_ad_minutes = num_ad_breaks * ad_break_duration

    # L4
    total_non_song_minutes = total_talking_minutes + total_ad_minutes

    # L5
    song_play_minutes = total_show_minutes - total_non_song_minutes

    # FA
    answer = song_play_minutes
    return answer