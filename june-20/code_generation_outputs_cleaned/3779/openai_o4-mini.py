def solve(
        green_beads: int = 3, # pattern has 3 green beads
        purple_beads: int = 5, # pattern has 5 purple beads
        red_beads_ratio: int = 2, # twice as many red beads as green beads
        repeats_per_bracelet: int = 3, # pattern repeats three times per bracelet
        repeats_per_necklace: int = 5, # pattern repeats 5 times per necklace
        num_bracelets: int = 1, # make 1 bracelets
        num_necklaces: int = 10 # make 10 necklaces
    ):
    """Index: 3779.
    Returns: the total number of beads needed to make 1 bracelet and 10 necklaces."""
    #: L1
    red_beads_per_repeat = green_beads * red_beads_ratio
    #: L2
    beads_per_repeat = red_beads_per_repeat + green_beads + purple_beads
    #: L3
    beads_per_bracelet = beads_per_repeat * repeats_per_bracelet
    #: L4
    beads_per_necklace = beads_per_repeat * repeats_per_necklace
    #: L5
    total_beads_necklaces = beads_per_necklace * num_necklaces
    #: L6
    total_beads = total_beads_necklaces + beads_per_bracelet * num_bracelets
    answer = total_beads # FINAL ANSWER
    return answer