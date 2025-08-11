def solve():
    """Index: 3928.
    Returns: the number of houses that can be painted.
    """
    # L1
    hours = 3 # 3 hours
    minutes_per_hour = 60 # WK
    total_minutes = hours * minutes_per_hour

    # L2
    time_per_house = 20 # 20 minutes to paint a house
    num_houses = total_minutes / time_per_house

    # FA
    answer = num_houses
    return answer