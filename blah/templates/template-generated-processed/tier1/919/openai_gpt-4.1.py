def solve():
    """Index: 919.
    Returns: the number of songs on Aisha's mp3 player now.
    """
    # L1
    songs_first_week = 500 # starts with 500 songs
    songs_second_week = 500 # adds another 500 the week after that
    songs_after_two_weeks = songs_first_week + songs_second_week

    # L2
    multiplier = 2 # adds twice the amount she already had
    songs_added_after = songs_after_two_weeks * multiplier

    # L3
    total_songs_before_removal = songs_after_two_weeks + songs_added_after

    # L4
    songs_removed = 50 # removes 50 songs
    songs_now = total_songs_before_removal - songs_removed

    # FA
    answer = songs_now
    return answer