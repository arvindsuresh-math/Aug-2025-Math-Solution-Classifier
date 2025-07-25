def solve():
    """Index: 2944.
    Returns: Jane's speed in meters per minute.
    """
    # L1
    kilometers_run = 3 # Jane runs 3 kilometers
    meters_per_kilometer = 1000 # 1 kilometer is equal to 1000 meters
    distance_meters = kilometers_run * meters_per_kilometer

    # L2
    hours_run = 2 # two hours
    minutes_per_hour = 60 # an hour has 60 minutes
    time_minutes = hours_run * minutes_per_hour

    # L3
    speed_meters_per_minute = distance_meters / time_minutes

    # FA
    answer = speed_meters_per_minute
    return answer