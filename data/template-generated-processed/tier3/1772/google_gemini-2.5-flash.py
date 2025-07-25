def solve():
    """Index: 1772.
    Returns: the total number of hours Tod drove.
    """
    # L1
    distance_north = 55 # 55 miles to the north
    distance_west = 95 # 95 miles to the west
    total_distance = distance_north + distance_west

    # L2
    speed = 25 # constantly drives 25 miles an hour
    total_hours = total_distance / speed

    # FA
    answer = total_hours
    return answer