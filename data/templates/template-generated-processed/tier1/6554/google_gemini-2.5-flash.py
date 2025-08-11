def solve():
    """Index: 6554.
    Returns: the number of silver beads Michelle uses.
    """
    # L1
    blue_beads = 5 # 5 blue beads
    red_beads_multiplier = 2 # 2 times as many red beads as blue beads
    red_beads = blue_beads * red_beads_multiplier

    # L2
    white_beads = blue_beads + red_beads

    # L3
    total_colored_beads = blue_beads + red_beads + white_beads

    # L4
    total_beads_necklace = 40 # 40 beads in making a necklace
    silver_beads = total_beads_necklace - total_colored_beads

    # FA
    answer = silver_beads
    return answer