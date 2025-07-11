def solve():
    """Index: 1124.
    Returns: the total number of pieces of clothing to put in the washer.
    """
    # L1
    total_blouses = 12 # 12 blouses
    blouses_hamper_percent_num = 75 # 75% of her blouses
    percent_factor = 0.01 # WK
    blouses_in_hamper = total_blouses * blouses_hamper_percent_num * percent_factor

    # L2
    total_skirts = 6 # 6 skirts
    skirts_hamper_percent_num = 50 # 50% of her skirts
    skirts_in_hamper = total_skirts * skirts_hamper_percent_num * percent_factor

    # L3
    total_slacks = 8 # 8 slacks
    slacks_hamper_percent_num = 25 # 25% of her slacks
    slacks_in_hamper = total_slacks * slacks_hamper_percent_num * percent_factor

    # L4
    total_pieces_to_wash = blouses_in_hamper + skirts_in_hamper + slacks_in_hamper

    # FA
    answer = total_pieces_to_wash
    return answer