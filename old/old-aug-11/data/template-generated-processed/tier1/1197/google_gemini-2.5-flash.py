def solve():
    """Index: 1197.
    Returns: the number of additional beads Bella needs.
    """
    # L1
    beads_per_bracelet = 8 # 8 beads per bracelet
    num_friends = 6 # 6 friends
    total_beads_needed = beads_per_bracelet * num_friends

    # L2
    beads_has = 36 # She has 36 beads
    beads_needed_more = total_beads_needed - beads_has

    # FA
    answer = beads_needed_more
    return answer