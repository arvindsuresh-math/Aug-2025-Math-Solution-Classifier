def solve():
    """Index: 1741.
    Returns: the total liters of water the farmer can carry in his trucks.
    """
    # L1
    tanks_per_truck = 3 # three tanks
    liters_per_tank = 150 # capacity of 150 liters of water
    liters_per_truck = tanks_per_truck * liters_per_tank

    # L2
    num_trucks = 3 # three trucks
    total_liters = num_trucks * liters_per_truck

    # FA
    answer = total_liters
    return answer