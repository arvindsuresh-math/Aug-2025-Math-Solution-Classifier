def solve():
    """Index: 4248.
    Returns: the number of additional complete laps Albert will have made.
    """
    # L1
    total_distance_to_run = 99 # Albert has to run 99 meters
    track_length_per_lap = 9 # The track is 9 meters around
    total_laps_needed = total_distance_to_run / track_length_per_lap

    # L2
    laps_already_run = 6 # He has already run 6 times around it
    remaining_laps = total_laps_needed - laps_already_run

    # FA
    answer = remaining_laps
    return answer