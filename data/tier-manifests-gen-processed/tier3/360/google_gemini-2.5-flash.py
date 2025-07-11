def solve():
    """Index: 360.
    Returns: the total ounces of oil used.
    """
    # L1
    oil_per_ratio = 2 # two ounces of oil
    peanuts_per_ratio = 8 # every eight ounces of peanuts
    total_per_ratio = oil_per_ratio + peanuts_per_ratio

    # L2
    last_batch_weight = 20 # Her last batch of peanut butter weighed 20 ounces
    ratio_multiplier = last_batch_weight / total_per_ratio

    # L3
    total_oil_used = oil_per_ratio * ratio_multiplier

    # FA
    answer = total_oil_used
    return answer