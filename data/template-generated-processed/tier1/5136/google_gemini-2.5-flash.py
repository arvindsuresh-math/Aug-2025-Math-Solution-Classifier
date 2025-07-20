def solve():
    """Index: 5136.
    Returns: the total number of blossoms Mario has.
    """
    # L1
    flowers_first_plant = 2 # The first hibiscus plant has 2 flowers
    multiplier_second_plant = 2 # twice as many flowers
    flowers_second_plant = flowers_first_plant * multiplier_second_plant

    # L2
    multiplier_third_plant = 4 # four times as many flowers
    flowers_third_plant = flowers_second_plant * multiplier_third_plant

    # L3
    total_blossoms = flowers_first_plant + flowers_second_plant + flowers_third_plant

    # FA
    answer = total_blossoms
    return answer