def solve():
    """Index: 2926.
    Returns: how much faster Mac will run the race in minutes.
    """
    # L1
    race_distance = 24 # a 24 mile race
    apple_speed = 3 # Apple can run at a rate of 3 miles per hour
    apple_time_hours = race_distance / apple_speed

    # L2
    mac_speed = 4 # Mac can run at a rate of 4 miles per hour
    mac_time_hours = race_distance / mac_speed

    # L3
    time_difference_hours = apple_time_hours - mac_time_hours

    # L4
    minutes_per_hour = 60 # 1 hour = 60 minutes
    time_difference_minutes = time_difference_hours * minutes_per_hour

    # FA
    answer = time_difference_minutes
    return answer