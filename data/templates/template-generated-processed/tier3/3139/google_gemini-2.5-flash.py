def solve():
    """Index: 3139.
    Returns: the total number of beads Charley pulled out.
    """
    # L1
    total_black_beads = 90 # 90 black beads
    black_beads_divisor = 6 # 1/6 of the black beads
    pulled_out_black_beads = total_black_beads / black_beads_divisor

    # L2
    total_white_beads = 51 # 51 white beads
    white_beads_divisor = 3 # a third of the white beads
    pulled_out_white_beads = total_white_beads / white_beads_divisor

    # L3
    total_pulled_out_beads = pulled_out_black_beads + pulled_out_white_beads

    # FA
    answer = total_pulled_out_beads
    return answer