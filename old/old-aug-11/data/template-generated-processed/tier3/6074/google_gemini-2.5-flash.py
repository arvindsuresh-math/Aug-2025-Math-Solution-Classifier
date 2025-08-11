def solve():
    """Index: 6074.
    Returns: the number of Legos remaining in the box.
    """
    # L1
    initial_legos = 500 # 500 Legos
    half_divisor = 2 # half the pieces
    unused_legos = initial_legos / half_divisor

    # L2
    missing_pieces = 5 # 5 missing pieces
    legos_in_box = unused_legos - missing_pieces

    # FA
    answer = legos_in_box
    return answer