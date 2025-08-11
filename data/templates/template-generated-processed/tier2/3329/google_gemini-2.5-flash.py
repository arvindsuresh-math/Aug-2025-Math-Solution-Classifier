def solve():
    """Index: 3329.
    Returns: the number of clear pieces of glass.
    """
    # L1
    green_pieces = 35 # 35 green pieces
    green_percent_decimal = 0.25 # 25% of the total glass he sweeps up
    total_pieces = green_pieces / green_percent_decimal

    # L2
    amber_pieces = 20 # 20 amber pieces
    clear_pieces = total_pieces - amber_pieces - green_pieces

    # FA
    answer = clear_pieces
    return answer