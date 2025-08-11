def solve():
    """Index: 5162.
    Returns: the additional hours needed to travel the additional distance.
    """
    # L1
    initial_distance = 360 # travels 360 miles
    initial_time = 3 # in 3 hours
    rate = initial_distance / initial_time

    # L2
    additional_distance = 240 # travel an additional 240 miles
    additional_hours = additional_distance / rate

    # FA
    answer = additional_hours
    return answer