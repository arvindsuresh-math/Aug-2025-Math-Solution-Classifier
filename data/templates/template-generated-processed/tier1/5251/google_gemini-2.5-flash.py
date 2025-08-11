def solve():
    """Index: 5251.
    Returns: the initial number of pieces the cake had.
    """
    # L1
    snack_pieces = 1 # ate one piece as a midnight snack
    multiplier_left_after_snack = 2 # Twice as many pieces as her snack were left
    pieces_left_after_snack = multiplier_left_after_snack * snack_pieces

    # L2
    pieces_before_snack = pieces_left_after_snack + snack_pieces

    # L3
    multiplier_half_leftovers = 2 # shared half the leftovers
    pieces_before_sharing_brothers = pieces_before_snack * multiplier_half_leftovers

    # L4
    multiplier_half_party_leftovers = 2 # guests ate half the cake
    initial_cake_pieces = multiplier_half_party_leftovers * pieces_before_sharing_brothers

    # FA
    answer = initial_cake_pieces
    return answer