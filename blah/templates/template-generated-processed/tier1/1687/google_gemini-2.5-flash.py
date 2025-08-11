def solve():
    """Index: 1687.
    Returns: the number of additional kilograms that can be loaded into the truck.
    """
    # L1
    num_bags = 100 # 100 bags of lemons
    mass_per_bag = 8 # 8 kilograms
    total_weight_lemons = num_bags * mass_per_bag

    # L2
    max_load = 900 # 900 kilograms
    remaining_capacity = max_load - total_weight_lemons

    # FA
    answer = remaining_capacity
    return answer