def solve():
    """Index: 157.
    Returns: the number of beads removed from each part.
    """
    # L1
    blue_beads = 23 # 23 blue beads
    yellow_beads = 16 # 16 yellow beads
    total_beads = blue_beads + yellow_beads

    # L2
    num_parts = 3 # divides the total into 3 equal parts
    beads_per_part_initial = total_beads / num_parts

    # L3
    beads_per_part_final = 6 # 6 beads in each part now
    doubling_factor = 2 # doubles the rest
    beads_left_before_doubling = beads_per_part_final / doubling_factor

    # L4
    beads_removed_per_part = beads_per_part_initial - beads_left_before_doubling

    # FA
    answer = beads_removed_per_part
    return answer