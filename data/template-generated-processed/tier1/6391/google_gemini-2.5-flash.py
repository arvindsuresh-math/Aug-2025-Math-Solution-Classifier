def solve():
    """Index: 6391.
    Returns: the number of puzzle pieces that are missing.
    """
    # L1
    total_pieces = 500 # 500 piece puzzle
    border_pieces = 75 # border used 75 pieces
    pieces_after_border = total_pieces - border_pieces

    # L2
    trevor_pieces = 105 # Trevor was able to place 105 pieces
    joe_multiplier = 3 # three times the number of puzzle pieces as Trevor
    joe_pieces = joe_multiplier * trevor_pieces

    # L3
    total_placed_by_trevor_joe = joe_pieces + trevor_pieces

    # L4
    missing_pieces = pieces_after_border - total_placed_by_trevor_joe

    # FA
    answer = missing_pieces
    return answer