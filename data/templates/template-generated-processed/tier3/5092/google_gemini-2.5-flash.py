def solve():
    """Index: 5092.
    Returns: how much faster Kevin must travel.
    """
    # L1
    total_distance = 600 # a 600-mile trip
    current_rate = 50 # traveling at a rate of 50 miles per hour
    current_travel_time = total_distance / current_rate

    # L2
    time_decrease = 4 # decrease his travel time by 4 hours
    desired_travel_time = current_travel_time - time_decrease

    # L3
    new_rate = total_distance / desired_travel_time

    # L4
    speed_increase = new_rate - current_rate

    # FA
    answer = speed_increase
    return answer