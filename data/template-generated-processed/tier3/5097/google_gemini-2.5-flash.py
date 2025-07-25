def solve():
    """Index: 5097.
    Returns: the number of gemstone samples Joan has.
    """
    # L1
    minerals_now = 48 # If she has 48 minerals now
    found_minerals = 6 # found 6 more mineral samples
    minerals_yesterday = minerals_now - found_minerals

    # L2
    gemstone_ratio_denominator = 2 # half as many gemstones
    gemstone_samples = minerals_yesterday / gemstone_ratio_denominator

    # FA
    answer = gemstone_samples
    return answer