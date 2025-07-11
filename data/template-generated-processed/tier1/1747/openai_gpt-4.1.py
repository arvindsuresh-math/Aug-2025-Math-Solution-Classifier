def solve():
    """Index: 1747.
    Returns: how many more marbles Markus has than Mara.
    """
    # L1
    mara_bags = 12 # Mara has 12 bags
    mara_marbles_per_bag = 2 # 2 marbles in each bag
    mara_total = mara_marbles_per_bag * mara_bags

    # L2
    markus_bags = 2 # Markus has 2 bags
    markus_marbles_per_bag = 13 # 13 marbles in each bag
    markus_total = markus_bags * markus_marbles_per_bag

    # L3
    difference = markus_total - mara_total

    # FA
    answer = difference
    return answer