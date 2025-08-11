def solve():
    """Index: 4322.
    Returns: the time saved on the trip.
    """
    # L1
    total_distance = 1200 # 1200-mile trip
    speed_faster = 60 # 60 miles an hour
    time_faster_speed = total_distance / speed_faster

    # L2
    speed_slower = 50 # 50 miles an hour
    time_slower_speed = total_distance / speed_slower

    # L3
    time_saved = time_slower_speed - time_faster_speed

    # FA
    answer = time_saved
    return answer