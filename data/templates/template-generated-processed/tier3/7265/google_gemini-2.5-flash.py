def solve():
    """Index: 7265.
    Returns: the number of chocolate pieces Mandy will get.
    """
    # L1
    total_pieces = 60 # 60 pieces
    michael_share_divisor = 2 # half of the bar
    michael_pieces = total_pieces / michael_share_divisor

    # L2
    paige_share_divisor = 2 # half of the remainder
    paige_pieces = michael_pieces / paige_share_divisor

    # L3
    mandy_pieces = total_pieces - michael_pieces - paige_pieces

    # FA
    answer = mandy_pieces
    return answer