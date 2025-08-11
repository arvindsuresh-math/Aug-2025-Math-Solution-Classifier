def solve():
    """Index: 5340.
    Returns: the total time it takes James to run 100 meters.
    """
    # L1
    total_race_distance = 100 # 100 meters
    john_initial_distance = 4 # 4 meters in the first second
    john_remaining_distance = total_race_distance - john_initial_distance

    # L2
    john_total_time = 13 # 13 seconds
    john_initial_time = 1 # first second
    john_remaining_time = john_total_time - john_initial_time

    # L3
    john_speed = john_remaining_distance / john_remaining_time

    # L4
    james_speed_increase = 2 # 2 m/s faster
    james_top_speed = john_speed + james_speed_increase

    # L5
    james_initial_distance = 10 # first 10 meters
    james_remaining_distance = total_race_distance - james_initial_distance

    # L6
    james_remaining_time = james_remaining_distance / james_top_speed

    # L7
    james_initial_time = 2 # first 10 meters in 2 seconds
    james_total_time = james_remaining_time + james_initial_time

    # FA
    answer = james_total_time
    return answer