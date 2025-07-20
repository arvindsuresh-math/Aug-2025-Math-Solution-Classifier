def solve():
    """Index: 5830.
    Returns: the total time in minutes to finish all songs in the album.
    """
    # L1
    initial_songs = 25 # 25 songs
    added_songs = 10 # adds 10 more songs
    total_songs = initial_songs + added_songs

    # L2
    song_duration_minutes = 3 # each song is 3 minutes long
    total_time_minutes = total_songs * song_duration_minutes

    # FA
    answer = total_time_minutes
    return answer