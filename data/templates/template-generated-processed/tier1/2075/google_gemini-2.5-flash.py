def solve():
    """Index: 2075.
    Returns: the distance from the father's end of the hallway where they will meet.
    """
    # L3
    hallway_length = 16 # hallway that is 16m long
    father_speed_ratio = 3 # father is walking three times as fast
    son_speed_ratio = 1 # implied by 'three times as fast as the son'
    distance_portion = hallway_length / (father_speed_ratio + son_speed_ratio)

    # L4
    father_distance_from_end = father_speed_ratio * distance_portion

    # FA
    answer = father_distance_from_end
    return answer