def solve():
    """Index: 5173.
    Returns: the total length of the tape in minutes.
    """
    # L1
    side_one_songs = 6 # The first side has 6 songs.
    side_two_songs = 4 # The second side has 4 songs.
    total_songs = side_one_songs + side_two_songs

    # L2
    song_duration_minutes = 4 # Each song is 4 minutes.
    total_tape_length = total_songs * song_duration_minutes

    # FA
    answer = total_tape_length
    return answer