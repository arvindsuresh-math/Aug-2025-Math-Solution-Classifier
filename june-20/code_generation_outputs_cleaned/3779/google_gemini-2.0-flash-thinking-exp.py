def solve(
    num_green_beads: int = 3, # 3 green beads
    num_purple_beads: int = 5, # 5 purple beads
    red_beads_multiplier: int = 2, # twice as many red beads as green beads
    repeats_per_bracelet: int = 3, # pattern repeats three times per bracelet
    repeats_per_necklace: int = 5, # 5 times per necklace
    num_bracelets: int = 1, # make 1 bracelets
    num_necklaces: int = 10 # and 10 necklaces
):
    """Index: 3779.
    Returns: the total number of beads needed to make the specified number of bracelets and necklaces.
    """
    #: L1
    num_red_beads_per_repeat = num_green_beads * red_beads_multiplier

    #: L2
    total_beads_per_repeat = num_red_beads_per_repeat + num_green_beads + num_purple_beads

    #: L3
    beads_per_bracelet = total_beads_per_repeat * repeats_per_bracelet

    #: L4
    beads_per_necklace = total_beads_per_repeat * repeats_per_necklace

    #: L5
    total_beads_necklaces = beads_per_necklace * num_necklaces

    #: L6
    total_beads_bracelets = beads_per_bracelet * num_bracelets
    total_beads_used = total_beads_necklaces + total_beads_bracelets

    answer = total_beads_used # FINAL ANSWER
    return answer