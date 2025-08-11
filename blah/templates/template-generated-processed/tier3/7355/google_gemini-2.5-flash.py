def solve():
    """Index: 7355.
    Returns: the number of four-minute songs Minnie needs to add.
    """
    # L1
    total_playlist_minutes = 60 # An hour is equal to 60 minutes

    # L2
    num_three_minute_songs = 16 # added 16 three-minute songs
    duration_three_minute_song = 3 # three-minute songs
    minutes_already_on_playlist = num_three_minute_songs * duration_three_minute_song

    # L3
    minutes_to_fill = total_playlist_minutes - minutes_already_on_playlist

    # L4
    duration_four_minute_song = 4 # four-minute songs
    num_four_minute_songs_needed = minutes_to_fill / duration_four_minute_song

    # FA
    answer = num_four_minute_songs_needed
    return answer