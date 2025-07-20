def solve():
    """Index: 6678.
    Returns: the number of citrus orchards growing grapefruits.
    """
    # L1
    lemons_orchards = 8 # Lemons, their most popular citrus fruit, will take up eight orchards
    orange_divisor = 2 # half as many orchards as the lemons
    orange_orchards = lemons_orchards / orange_divisor

    # L2
    total_orchards = 16 # sixteen orchards
    remaining_orchards = total_orchards - lemons_orchards - orange_orchards

    # L3
    split_divisor = 2 # Limes and grapefruits will split the remaining orchards
    grapefruit_orchards = remaining_orchards / split_divisor

    # FA
    answer = grapefruit_orchards
    return answer