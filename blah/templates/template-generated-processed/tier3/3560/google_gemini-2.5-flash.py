def solve():
    """Index: 3560.
    Returns: the number of lettuce plants Anna should grow.
    """
    # L1
    target_salads = 12 # at least 12 large salads
    salads_per_plant = 3 # Each lettuce plant is estimated to provide 3 large salads
    plants_without_loss = target_salads / salads_per_plant

    # L2
    loss_factor = 2 # half of the lettuce will be lost to insects and rabbits
    total_plants_needed = plants_without_loss * loss_factor

    # FA
    answer = total_plants_needed
    return answer