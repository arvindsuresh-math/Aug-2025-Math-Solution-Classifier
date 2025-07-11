def solve():
    """Index: 1046.
    Returns: the number of flowers remaining in the vase.
    """
    # L1
    num_dozens = 3 # 3 dozen roses
    roses_per_dozen = 12 # WK
    total_initial_roses = num_dozens * roses_per_dozen

    # L2
    half_divisor = 2 # half to her daughter
    roses_given_to_daughter = total_initial_roses / half_divisor

    # L3
    roses_in_vase_initial = total_initial_roses - roses_given_to_daughter

    # L4
    wilted_fraction_denominator = 3 # one-third of the flowers
    wilted_flowers = roses_in_vase_initial / wilted_fraction_denominator

    # L5
    flowers_remaining_in_vase = roses_in_vase_initial - wilted_flowers

    # FA
    answer = flowers_remaining_in_vase
    return answer