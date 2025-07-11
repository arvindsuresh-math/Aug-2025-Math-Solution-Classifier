def solve():
    """Index: 1194.
    Returns: the length of the pieces of rope after all operations.
    """
    # L1
    total_rope_length = 72 # 72 inches of rope
    num_pieces = 12 # cuts it into 12 equal length pieces
    length_per_piece = total_rope_length / num_pieces

    # L2
    knot_shortening = 1 # each piece 1 inch shorter
    length_after_knots = length_per_piece - knot_shortening

    # L3
    num_pieces_tied = 3 # ties three pieces together
    total_length_tied_pieces = length_after_knots * num_pieces_tied

    # FA
    answer = total_length_tied_pieces
    return answer