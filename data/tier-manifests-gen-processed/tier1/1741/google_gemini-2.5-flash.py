def solve():
    """Index: 1741.
    Returns: the total liters of water the farmer can carry in his trucks.
    """
    # L1
    tanks_per_truck = 3 # Each truck uses three tanks
    capacity_per_tank = 150 # capacity of 150 liters of water
    capacity_per_truck = tanks_per_truck * capacity_per_tank

    # L2
    num_trucks = 3 # three trucks
    total_capacity = num_trucks * capacity_per_truck

    # FA
    answer = total_capacity
    return answer