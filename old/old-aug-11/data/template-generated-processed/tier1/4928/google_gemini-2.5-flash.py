def solve():
    """Index: 4928.
    Returns: the number of swans in the pond after ten years.
    """
    # L1
    current_swans = 15 # Currently, there are 15 swans in the pond
    doubling_factor = 2 # the number of swans at Rita's pond doubles
    swans_after_2_years = current_swans * doubling_factor

    # L2
    swans_after_4_years = doubling_factor * swans_after_2_years

    # L3
    swans_after_6_years = doubling_factor * swans_after_4_years

    # L4
    swans_after_8_years = doubling_factor * swans_after_6_years

    # L5
    swans_after_10_years = doubling_factor * swans_after_8_years

    # FA
    answer = swans_after_10_years
    return answer