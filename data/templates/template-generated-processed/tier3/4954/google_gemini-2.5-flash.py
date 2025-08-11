def solve():
    """Index: 4954.
    Returns: the cost of one of the other pieces of clothing.
    """
    # L1
    total_spent = 610 # Jangshe spent $610
    cost_piece1 = 49 # One piece was $49
    remaining_after_piece1 = total_spent - cost_piece1
    cost_piece2 = 81 # another piece was $81
    remaining_after_piece2 = remaining_after_piece1 - cost_piece2

    # L2
    total_pieces = 7 # 7 pieces of clothing
    known_pieces = 2 # One piece was $49 and another piece was $81
    other_pieces_count = total_pieces - known_pieces

    # L3
    cost_per_other_piece = remaining_after_piece2 / other_pieces_count

    # FA
    answer = cost_per_other_piece
    return answer