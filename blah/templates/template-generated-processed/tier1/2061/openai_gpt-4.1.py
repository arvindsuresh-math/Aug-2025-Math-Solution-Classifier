def solve():
    """Index: 2061.
    Returns: the total distance each player will run in meters.
    """
    # L1
    length = 100 # length 100 m
    width = 50 # width 50 m
    perimeter = 2 * length + 2 * width

    # L2
    num_laps = 6 # six laps
    total_distance = num_laps * perimeter

    # FA
    answer = total_distance
    return answer