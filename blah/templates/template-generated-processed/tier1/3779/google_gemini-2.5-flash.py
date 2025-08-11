def solve():
    """Index: 3779.
    Returns: the total number of beads needed to make 1 bracelet and 10 necklaces.
    """
    # L1
    green_beads_per_repeat = 3 # 3 green beads
    red_beads_multiplier = 2 # twice as many red beads as green beads
    red_beads_per_repeat = green_beads_per_repeat * red_beads_multiplier

    # L2
    purple_beads_per_repeat = 5 # 5 purple beads
    total_beads_per_repeat = red_beads_per_repeat + green_beads_per_repeat + purple_beads_per_repeat

    # L3
    repeats_per_bracelet = 3 # pattern repeats three times per bracelet
    beads_per_bracelet = total_beads_per_repeat * repeats_per_bracelet

    # L4
    repeats_per_necklace = 5 # 5 times per necklace
    beads_per_necklace = total_beads_per_repeat * repeats_per_necklace

    # L5
    num_necklaces = 10 # 10 necklaces
    total_beads_necklaces = beads_per_necklace * num_necklaces

    # L6
    num_bracelets = 1 # 1 bracelets
    total_beads_used = total_beads_necklaces + beads_per_bracelet

    # FA
    answer = total_beads_used
    return answer