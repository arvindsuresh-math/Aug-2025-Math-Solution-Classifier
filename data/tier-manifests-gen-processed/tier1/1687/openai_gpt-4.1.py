def solve():
    """Index: 1687.
    Returns: how many more kilograms can still be loaded into the truck.
    """
    # L1
    num_bags = 100 # 100 bags of lemons
    mass_per_bag = 8 # mass of 8 kilograms per bag
    total_weight = num_bags * mass_per_bag

    # L2
    max_truck_load = 900 # load on a truck may not be more than 900 kilograms
    remaining_capacity = max_truck_load - total_weight

    # FA
    answer = remaining_capacity
    return answer