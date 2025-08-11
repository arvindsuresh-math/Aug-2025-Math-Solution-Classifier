def solve():
    """Index: 1197.
    Returns: the number of additional beads Bella needs to make all six bracelets.
    """
    # L1
    beads_per_bracelet = 8 # 8 beads per bracelet
    num_friends = 6 # 6 friends
    total_beads_needed = beads_per_bracelet * num_friends

    # L2
    beads_on_hand = 36 # She has 36 beads
    beads_needed = total_beads_needed - beads_on_hand

    # FA
    answer = beads_needed
    return answer