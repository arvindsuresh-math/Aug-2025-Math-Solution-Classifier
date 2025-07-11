def solve():
    """Index: 648.
    Returns: the average number of songs played in the third and fourth sets.
    """
    # L1
    first_set_songs = 5 # played 5 songs in their first set
    second_set_songs = 7 # and 7 in their second set
    songs_in_first_two_sets = first_set_songs + second_set_songs

    # L2
    total_repertoire_songs = 30 # The school band has 30 songs in their repertoire
    songs_left_after_two_sets = total_repertoire_songs - songs_in_first_two_sets

    # L3
    encore_songs = 2 # The band will play 2 songs for their encore
    songs_for_third_fourth_sets = songs_left_after_two_sets - encore_songs

    # L4
    number_of_sets_for_average = 2 # third and fourth sets
    average_songs_per_set = songs_for_third_fourth_sets / number_of_sets_for_average

    # FA
    answer = average_songs_per_set
    return answer