def solve():
    """Index: 3668.
    Returns: the number of green tea leaves needed for the same efficacy.
    """
    # L1
    sprigs_of_mint_per_batch = 3 # three sprigs of mint
    green_tea_leaves_per_sprig = 2 # two green tea leaves for every sprig of mint
    green_tea_leaves_per_batch_old_mud = sprigs_of_mint_per_batch * green_tea_leaves_per_sprig

    # L2
    multiplier_for_half_effectiveness = 2 # half as effective
    green_tea_leaves_new_mud = green_tea_leaves_per_batch_old_mud * multiplier_for_half_effectiveness

    # FA
    answer = green_tea_leaves_new_mud
    return answer