def solve():
    """Index: 6054.
    Returns: the number of fish the twentieth fisherman caught.
    """
    # L1
    fish_per_fisherman_group_1 = 400 # caught 400 fish each
    num_fishermen_group_1 = 19 # 19 of them caught
    total_fish_group_1 = fish_per_fisherman_group_1 * num_fishermen_group_1

    # L2
    total_fish_caught = 10000 # 10000 fish in total
    fish_twentieth_fisherman = total_fish_caught - total_fish_group_1

    # FA
    answer = fish_twentieth_fisherman
    return answer