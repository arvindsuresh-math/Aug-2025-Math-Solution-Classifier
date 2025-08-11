def solve():
    """Index: 634.
    Returns: the combined total number of stripes Vaishali has on all of her hats.
    """
    # L1
    num_hats_group1 = 4 # 4 hats
    stripes_per_hat_group1 = 3 # three stripes
    stripes_group1 = num_hats_group1 * stripes_per_hat_group1

    # L2
    num_hats_group2 = 3 # three hats
    stripes_per_hat_group2 = 4 # four stripes each
    stripes_group2 = num_hats_group2 * stripes_per_hat_group2

    # L3
    num_hats_group3 = 6 # six hats
    stripes_per_hat_group3 = 0 # no stripes
    stripes_group3 = num_hats_group3 * stripes_per_hat_group3

    # L4
    num_hats_group4 = 2 # two hats
    stripes_per_hat_group4 = 5 # 5 stripes each
    stripes_group4 = num_hats_group4 * stripes_per_hat_group4

    # L5
    total_stripes = stripes_group1 + stripes_group2 + stripes_group3 + stripes_group4

    # FA
    answer = total_stripes
    return answer