def solve():
    """Index: 3664.
    Returns: Bob's average speed in m/s.
    """
    # L1
    lap_length = 400 # track is 400 meters
    num_laps = 3 # 3 laps
    total_distance = lap_length * num_laps

    # L2
    first_lap_time = 70 # first lap in 70 seconds
    second_lap_time = 85 # second and third lap in 85 seconds each
    third_lap_time = 85 # second and third lap in 85 seconds each
    total_time = first_lap_time + second_lap_time + third_lap_time

    # L3
    average_speed = total_distance / total_time

    # FA
    answer = average_speed
    return answer