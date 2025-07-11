def solve():
    """Index: 2008.
    Returns: the number of dives Jamie has to make to collect 56 pearls.
    """
    # L1
    pearl_probability = 0.25 # 25% of oysters have pearls in them
    oysters_per_dive = 16 # Jamie can collect 16 oysters during each dive
    pearls_per_dive = pearl_probability * oysters_per_dive

    # L2
    pearls_needed = 56 # collect 56 pearls
    dives_needed = pearls_needed / pearls_per_dive

    # FA
    answer = dives_needed
    return answer