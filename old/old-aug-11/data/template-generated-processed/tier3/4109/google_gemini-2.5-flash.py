def solve():
    """Index: 4109.
    Returns: the total kilometers Kristine traveled.
    """
    # L1
    train_distance = 300 # driven a train for 300 km
    bus_distance_divisor = 2 # half that distance
    bus_distance = train_distance / bus_distance_divisor

    # L2
    cab_distance_divisor = 3 # three times fewer kilometers
    cab_distance = bus_distance / cab_distance_divisor

    # L3
    total_distance = bus_distance + cab_distance + train_distance

    # FA
    answer = total_distance
    return answer