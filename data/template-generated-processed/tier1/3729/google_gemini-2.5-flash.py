def solve():
    """Index: 3729.
    Returns: the additional minutes of songs Stan needs for his playlist.
    """
    # L1
    num_3_min_songs = 10 # 10 3-minute songs
    duration_3_min_song = 3 # 3-minute songs
    playtime_3_min_songs = num_3_min_songs * duration_3_min_song

    # L2
    num_2_min_songs = 15 # 15 2-minute songs
    duration_2_min_song = 2 # 2-minute songs
    playtime_2_min_songs = num_2_min_songs * duration_2_min_song

    # L3
    current_playlist_duration = playtime_3_min_songs + playtime_2_min_songs

    # L4
    total_run_duration = 100 # His entire run takes 100 minutes
    minutes_needed = total_run_duration - current_playlist_duration

    # FA
    answer = minutes_needed
    return answer