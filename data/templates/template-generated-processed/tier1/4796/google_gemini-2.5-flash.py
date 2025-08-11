def solve():
    """Index: 4796.
    Returns: the total number of tanks and trucks in the yard.
    """
    # L1
    tanks_multiplier = 5 # five times the number of trucks
    num_trucks = 20 # 20 trucks in the yard
    num_tanks = tanks_multiplier * num_trucks

    # L2
    total_vehicles = num_tanks + num_trucks

    # FA
    answer = total_vehicles
    return answer