def solve():
    """Index: 893.
    Returns: the total number of beads Kylie uses for her jewelry.
    """
    # L1
    necklaces_monday = 10 # 10 beaded necklaces on Monday
    necklaces_tuesday = 2 # 2 beaded necklaces on Tuesday
    total_necklaces = necklaces_monday + necklaces_tuesday

    # L2
    beads_per_necklace = 20 # 20 beads are needed to make one beaded necklace
    beads_for_necklaces = total_necklaces * beads_per_necklace

    # L3
    num_bracelets = 5 # 5 beaded bracelets
    beads_per_bracelet = 10 # 10 beads are needed to make one beaded bracelet
    beads_for_bracelets = num_bracelets * beads_per_bracelet

    # L4
    num_earrings = 7 # 7 beaded earrings
    beads_per_earring = 5 # 5 beads are needed to make one beaded earring
    beads_for_earrings = num_earrings * beads_per_earring

    # L5
    total_beads_used = beads_for_necklaces + beads_for_bracelets + beads_for_earrings

    # FA
    answer = total_beads_used
    return answer