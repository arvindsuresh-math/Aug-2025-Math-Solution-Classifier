def solve():
    """Index: 2414.
    Returns: the time it would take Amanda to run the length of the track.
    """
    # L1
    field_length = 2000 # 2000 meters in length
    field_time = 2 # 2 hours
    speed_meters_per_hour = field_length / field_time

    # L2
    track_length = 10000 # 10000-meter track
    time_for_track_hours = track_length / speed_meters_per_hour

    # FA
    answer = time_for_track_hours
    return answer