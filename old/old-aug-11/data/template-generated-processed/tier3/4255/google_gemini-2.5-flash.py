def solve():
    """Index: 4255.
    Returns: the total time the hike took in hours.
    """
    # L1
    distance_up = 12 # 12 miles to Mount Overlook
    pace_up = 4 # 4 miles per hour
    time_up = distance_up / pace_up

    # L2
    distance_down = 12 # returns
    pace_down = 6 # 6 miles per hour
    time_down = distance_down / pace_down

    # L3
    total_time = time_up + time_down

    # FA
    answer = total_time
    return answer