def solve():
    """Index: 5779.
    Returns: the total number of blue beads Betty has.
    """
    # L1
    total_red_beads = 30 # she has 30 red beads
    red_beads_per_set = 3 # 3 red beads for every 2 blue beads
    num_sets = total_red_beads / red_beads_per_set

    # L2
    blue_beads_per_set = 2 # 2 blue beads
    total_blue_beads = num_sets * blue_beads_per_set

    # FA
    answer = total_blue_beads
    return answer