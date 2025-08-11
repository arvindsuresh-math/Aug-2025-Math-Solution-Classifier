def solve():
    """Index: 361.
    Returns: the number of kilometers the ship was blown westward by the storm.
    """
    # L1
    travel_hours = 20 # 20 hours at a speed of 30 kilometers per hour
    speed_kph = 30 # 30 kilometers per hour
    eastward_distance = travel_hours * speed_kph

    # L2
    total_distance = 2 * eastward_distance

    # L3
    one_third_fraction = 1 / 3 # one-third of the way
    one_third_distance = one_third_fraction * total_distance

    # L4
    blown_distance = eastward_distance - one_third_distance

    # FA
    answer = blown_distance
    return answer