def solve():
    """Index: 648.
    Returns: the average number of songs played in the third and fourth sets.
    """
    # L1
    first_set_songs = 5 # band played 5 songs in their first set
    second_set_songs = 7 # 7 in their second set
    songs_first_two_sets = first_set_songs + second_set_songs

    # L2
    total_songs = 30 # 30 songs in their repertoire
    songs_left_after_two_sets = total_songs - songs_first_two_sets

    # L3
    encore_songs = 2 # band will play 2 songs for their encore
    songs_for_third_and_fourth = songs_left_after_two_sets - encore_songs

    # L4
    sets_remaining = 2 # third and fourth sets # WK
    average_songs_per_set = songs_for_third_and_fourth / sets_remaining

    # FA
    answer = average_songs_per_set
    return answer