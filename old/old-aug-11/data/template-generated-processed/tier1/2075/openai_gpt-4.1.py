def solve():
    """Index: 2075.
    Returns: the distance from the father's end of the hallway where they meet.
    """
    # L3
    hallway_length = 16 # hallway that is 16m long
    father_speed_ratio = 3 # father is walking three times as fast as the son
    son_speed_ratio = 1 # implied by the ratio 3:1
    total_ratio = father_speed_ratio + son_speed_ratio
    portion_length = hallway_length / total_ratio

    # L4
    father_distance = father_speed_ratio * portion_length

    # FA
    answer = father_distance
    return answer