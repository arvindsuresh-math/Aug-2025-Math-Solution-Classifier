def solve():
    """Index: 5219.
    Returns: the number of pieces Anne's boyfriend picks up.
    """
    # L1
    total_pieces = 60 # breaks it into 60 pieces
    swept_up_divisor = 2 # sweeps up half of them
    pieces_after_sweep = total_pieces / swept_up_divisor

    # L2
    cat_stolen_pieces = 3 # her cat steals 3 pieces
    pieces_after_cat = pieces_after_sweep - cat_stolen_pieces

    # L3
    boyfriend_fraction_denominator = 3 # her boyfriend picks up 1/3 of the remaining pieces
    boyfriend_picked_up_pieces = pieces_after_cat / boyfriend_fraction_denominator

    # FA
    answer = boyfriend_picked_up_pieces
    return answer