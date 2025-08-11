def solve():
    """Index: 7353.
    Returns: the total number of songs the singer sang.
    """
    # L1
    total_concert_minutes = 80 # one hour 20 minutes concert
    intermission_minutes = 10 # a 10-minute intermission
    singing_time_after_intermission = total_concert_minutes - intermission_minutes

    # L2
    long_song_minutes = 10 # one song that lasted 10 minutes
    singing_time_for_short_songs = singing_time_after_intermission - long_song_minutes

    # L3
    short_song_duration = 5 # all the songs were 5 minutes
    num_short_songs = singing_time_for_short_songs / short_song_duration

    # L4
    num_long_songs = 1 # one song that lasted 10 minutes
    total_songs = num_short_songs + num_long_songs

    # FA
    answer = total_songs
    return answer