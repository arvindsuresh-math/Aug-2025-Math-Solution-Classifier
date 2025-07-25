def solve():
    """Index: 6016.
    Returns: the number of additional laps they have to run.
    """
    # L1
    laps_per_person = 6 # each have run 6 laps
    total_laps_run = laps_per_person + laps_per_person

    # L2
    track_length = 150 # The track is 150 meters around
    meters_run = total_laps_run * track_length

    # L3
    total_distance_needed = 2400 # run a total of 2400 meters
    meters_remaining = total_distance_needed - meters_run

    # L4
    laps_remaining = meters_remaining / track_length

    # FA
    answer = laps_remaining
    return answer