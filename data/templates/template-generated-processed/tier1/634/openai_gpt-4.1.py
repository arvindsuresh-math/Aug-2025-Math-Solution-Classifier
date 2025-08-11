def solve():
    """Index: 634.
    Returns: the combined total number of stripes Vaishali has on all of her hats.
    """
    # L1
    hats_3_stripes = 4 # 4 hats, each with three stripes
    stripes_per_hat_3 = 3 # 4 hats, each with three stripes
    total_stripes_3 = hats_3_stripes * stripes_per_hat_3

    # L2
    hats_4_stripes = 3 # three hats with four stripes each
    stripes_per_hat_4 = 4 # three hats with four stripes each
    total_stripes_4 = hats_4_stripes * stripes_per_hat_4

    # L3
    hats_0_stripes = 6 # six hats with no stripes
    stripes_per_hat_0 = 0 # six hats with no stripes
    total_stripes_0 = hats_0_stripes * stripes_per_hat_0

    # L4
    hats_5_stripes = 2 # two hats with 5 stripes each
    stripes_per_hat_5 = 5 # two hats with 5 stripes each
    total_stripes_5 = hats_5_stripes * stripes_per_hat_5

    # L5
    combined_total = total_stripes_3 + total_stripes_4 + total_stripes_0 + total_stripes_5

    # FA
    answer = combined_total
    return answer