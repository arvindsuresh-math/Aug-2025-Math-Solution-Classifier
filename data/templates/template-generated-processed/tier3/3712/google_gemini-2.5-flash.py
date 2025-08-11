def solve():
    """Index: 3712.
    Returns: the time it takes Peter to rake 8 bags of leaves.
    """
    # L2
    initial_bags = 3 # 3 bags of leaves
    initial_time_minutes = 15 # 15 minutes
    target_bags = 8 # 8 bags
    product_of_knowns = initial_time_minutes * target_bags

    # L3
    time_to_rake_8_bags = product_of_knowns / initial_bags

    # FA
    answer = time_to_rake_8_bags
    return answer