def solve():
    """Index: 2008.
    Returns: the number of dives Jamie has to make.
    """
    # L1
    pearl_percentage_decimal = 0.25 # 25% of oysters have pearls in them
    oysters_per_dive = 16 # collect 16 oysters during each dive
    pearls_per_dive = pearl_percentage_decimal * oysters_per_dive

    # L2
    target_pearls = 56 # collect 56 pearls
    num_dives = target_pearls / pearls_per_dive

    # FA
    answer = num_dives
    return answer