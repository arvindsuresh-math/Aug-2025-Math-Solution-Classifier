def solve():
    """Index: 7343.
    Returns: the cost of each brownie piece.
    """
    # L1
    num_pans = 2 # 2 pans of brownies
    pieces_per_pan = 8 # cut into 8 big square pieces
    total_brownie_pieces = num_pans * pieces_per_pan

    # L2
    total_revenue = 32 # makes $32 from the brownies
    cost_per_brownie_piece = total_revenue / total_brownie_pieces

    # FA
    answer = cost_per_brownie_piece
    return answer