def solve():
    """Index: 6224.
    Returns: Eliza's height in inches.
    """
    # L1
    sibling_1_height = 66 # Two of her siblings are both 66 inches tall
    sibling_2_height = 66 # Two of her siblings are both 66 inches tall
    sibling_3_height = 60 # Another sibling is 60 inches tall
    height_first_three_siblings = sibling_1_height + sibling_2_height + sibling_3_height

    # L2
    total_height = 330 # The total height of all 5 siblings combined is 330 inches
    height_eliza_and_last_sibling = total_height - height_first_three_siblings

    # L4
    height_difference = 2 # Eliza is 2 inches shorter than the last sibling
    divisor_for_eliza_height = 2 # WK
    eliza_height = (height_eliza_and_last_sibling - height_difference) / divisor_for_eliza_height

    # FA
    answer = eliza_height
    return answer