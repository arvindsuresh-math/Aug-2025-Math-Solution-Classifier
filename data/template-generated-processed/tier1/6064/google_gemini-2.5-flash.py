def solve():
    """Index: 6064.
    Returns: the total number of beads in the necklace.
    """
    # L1
    purple_beads = 7 # 7 purple beads
    multiplier_for_blue = 2 # twice as many blue beads
    blue_beads = multiplier_for_blue * purple_beads

    # L2
    more_green_than_blue = 11 # 11 more green beads than blue beads
    green_beads = blue_beads + more_green_than_blue

    # L3
    total_beads = purple_beads + blue_beads + green_beads

    # FA
    answer = total_beads
    return answer