def solve():
    """Index: 7458.
    Returns: the average speed of Gerald's car in miles per hour.
    """
    # L1
    polly_circuits = 12 # 12 times
    polly_time_hours = 0.5 # one half hour
    polly_circuits_per_hour = polly_circuits / polly_time_hours

    # L2
    track_lengths_per_mile = 4 # WK
    polly_speed_mph = polly_circuits_per_hour / track_lengths_per_mile

    # L3
    gerald_speed_divisor = 2 # half of what Polly did
    gerald_speed_mph = polly_speed_mph / gerald_speed_divisor

    # FA
    answer = gerald_speed_mph
    return answer