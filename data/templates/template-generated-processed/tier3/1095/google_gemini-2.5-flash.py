def solve():
    """Index: 1095.
    Returns: the number of bicycles the friend owns.
    """
    # L1
    tires_per_bike = 2 # WK
    ignatius_bicycles = 4 # Ignatius owns 4 bicycles
    ignatius_total_tires = tires_per_bike * ignatius_bicycles

    # L2
    friend_tire_multiplier = 3 # three times are many tires
    friend_total_tires = friend_tire_multiplier * ignatius_total_tires

    # L3
    unicycle_tires = 1 # one unicycle
    tricycle_tires = 3 # a tricycle
    friend_bicycle_tires = friend_total_tires - unicycle_tires - tricycle_tires

    # L4
    friend_bicycles = friend_bicycle_tires / tires_per_bike

    # FA
    answer = friend_bicycles
    return answer