def solve():
    """Index: 5359.
    Returns: the number of times Cassie has to refill her water bottle.
    """
    # L1
    ounces_per_cup = 8 # 8 ounces of water in a cup
    target_cups = 12 # at least 12 cups of water a day
    total_ounces_needed = ounces_per_cup * target_cups

    # L2
    bottle_capacity_ounces = 16 # Her water bottle holds 16 ounces
    refills_needed = total_ounces_needed / bottle_capacity_ounces

    # FA
    answer = refills_needed
    return answer