def solve():
    """Index: 1314.
    Returns: the additional hours needed to travel the specified distance.
    """
    # L1
    total_distance_initial = 270 # travels 270 miles
    initial_time = 3 # in 3 hours
    rate = total_distance_initial / initial_time

    # L2
    additional_distance = 180 # travel an additional 180 miles
    additional_hours = additional_distance / rate

    # FA
    answer = additional_hours
    return answer