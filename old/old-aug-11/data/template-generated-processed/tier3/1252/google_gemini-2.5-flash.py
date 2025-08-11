def solve():
    """Index: 1252.
    Returns: the total number of bracelets Marnie can make.
    """
    # L1
    beads_per_small_bag = 50 # 50 beads
    num_small_bags = 5 # 5 bags
    beads_from_small_bags = beads_per_small_bag * num_small_bags

    # L2
    beads_per_large_bag = 100 # 100 beads
    num_large_bags = 2 # 2 bags
    beads_from_large_bags = beads_per_large_bag * num_large_bags

    # L3
    total_beads = beads_from_small_bags + beads_from_large_bags

    # L4
    beads_per_bracelet = 50 # 50 beads are used to make one bracelet
    num_bracelets = total_beads / beads_per_bracelet

    # FA
    answer = num_bracelets
    return answer