def solve():
    """Index: 5508.
    Returns: the total cost of the beads.
    """
    # L1
    purple_rows = 50 # 50 rows of purple beads
    purple_beads_per_row = 20 # 20 beads per row
    total_purple_beads = purple_rows * purple_beads_per_row

    # L2
    blue_rows = 40 # 40 rows of blue beads
    blue_beads_per_row = 18 # 18 beads per row
    total_blue_beads = blue_rows * blue_beads_per_row

    # L3
    gold_beads = 80 # 80 gold beads
    total_beads_needed = total_purple_beads + total_blue_beads + gold_beads

    # L4
    beads_per_dollar_unit = 10 # 10 beads
    total_cost = total_beads_needed / beads_per_dollar_unit

    # FA
    answer = total_cost
    return answer