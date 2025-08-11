def solve():
    """Index: 5067.
    Returns: the total cost of the foundation for all homes.
    """
    # L1
    slab_length = 100 # 100 feet
    slab_width = 100 # 100 feet
    slab_height = 0.5 # .5 feet
    slab_volume = slab_length * slab_width * slab_height

    # L2
    concrete_density = 150 # 150 pounds per cubic foot
    slab_weight = slab_volume * concrete_density

    # L3
    cost_per_pound = 0.02 # $.02 per pound
    cost_per_house = slab_weight * cost_per_pound

    # L4
    num_homes = 3 # 3 homes
    total_foundation_cost = cost_per_house * num_homes

    # FA
    answer = total_foundation_cost
    return answer