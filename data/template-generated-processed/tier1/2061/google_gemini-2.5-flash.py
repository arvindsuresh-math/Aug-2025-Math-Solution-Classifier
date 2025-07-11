def solve():
    """Index: 2061.
    Returns: the total distance each player will run in meters.
    """
    # L1
    field_length = 100 # length 100 m
    field_width = 50 # width 50 m
    perimeter_factor = 2 # WK
    distance_per_lap = perimeter_factor * field_length + perimeter_factor * field_width

    # L2
    num_laps = 6 # six laps
    total_distance = num_laps * distance_per_lap

    # FA
    answer = total_distance
    return answer