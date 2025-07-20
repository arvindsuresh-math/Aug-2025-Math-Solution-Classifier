def solve():
    """Index: 5410.
    Returns: the difference in hours between the fastest and slowest hike.
    """
    # L1
    trail_one_distance = 20 # One trail is 20 miles
    trail_one_speed = 5 # at 5 miles per hour
    trail_one_time = trail_one_distance / trail_one_speed

    # L2
    trail_two_distance = 12 # The other trail is 12 miles
    trail_two_speed = 3 # cover 3 miles per hour
    trail_two_hiking_time = trail_two_distance / trail_two_speed

    # L3
    break_time = 1 # take an hour break
    trail_two_total_time = trail_two_hiking_time + break_time

    # L4
    time_difference = trail_two_total_time - trail_one_time

    # FA
    answer = time_difference
    return answer