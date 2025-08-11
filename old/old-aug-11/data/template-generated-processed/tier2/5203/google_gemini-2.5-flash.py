def solve():
    """Index: 5203.
    Returns: the total number of times Lucy will jump rope.
    """
    # L1
    jumps_per_second = 1 # 1 time per second
    seconds_per_minute = 60 # WK
    jumps_per_minute = seconds_per_minute * jumps_per_second

    # L2
    num_songs = 10 # 10 songs
    song_length_minutes = 3.5 # 3.5 minutes long
    total_album_length_minutes = num_songs * song_length_minutes

    # L3
    total_jumps = total_album_length_minutes * jumps_per_minute

    # FA
    answer = total_jumps
    return answer