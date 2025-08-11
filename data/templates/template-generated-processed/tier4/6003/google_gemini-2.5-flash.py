def solve():
    """Index: 6003.
    Returns: the total time in minutes took to travel the whole journey.
    """
    # L1
    speed = 10 # 10 miles per hour
    distance_segment1 = 15 # another 15 miles
    time_segment1_hours = distance_segment1 / speed

    # L2
    minutes_per_hour = 60 # WK
    time_segment1_minutes = time_segment1_hours * minutes_per_hour

    # L3
    distance_segment2 = 20 # remaining distance of 20 miles
    time_segment2_hours = distance_segment2 / speed

    # L4
    time_segment2_minutes = time_segment2_hours * minutes_per_hour

    # L5
    initial_ride_time_minutes = 30 # for 30 minutes
    rest_time_minutes = 30 # rests for 30 minutes
    total_journey_time_minutes = initial_ride_time_minutes + time_segment1_minutes + rest_time_minutes + time_segment2_minutes

    # FA
    answer = total_journey_time_minutes
    return answer