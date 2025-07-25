def solve():
    """Index: 893.
    Returns: the total number of beads Kylie uses to make her jewelry.
    """
    # L1
    necklaces_monday = 10 # 10 beaded necklaces on Monday
    necklaces_tuesday = 2 # 2 beaded necklaces on Tuesday
    total_necklaces = necklaces_monday + necklaces_tuesday

    # L2
    beads_per_necklace = 20 # 20 beads are needed to make one beaded necklace
    beads_necklaces = total_necklaces * beads_per_necklace

    # L3
    bracelets_wednesday = 5 # 5 beaded bracelets on Wednesday
    beads_per_bracelet = 10 # 10 beads are needed to make one beaded bracelet
    beads_bracelets = bracelets_wednesday * beads_per_bracelet

    # L4
    earrings_wednesday = 7 # 7 beaded earrings on Wednesday
    beads_per_earring = 5 # 5 beads are needed to make one beaded earring
    beads_earrings = earrings_wednesday * beads_per_earring

    # L5
    total_beads = beads_necklaces + beads_bracelets + beads_earrings

    # FA
    answer = total_beads
    return answer