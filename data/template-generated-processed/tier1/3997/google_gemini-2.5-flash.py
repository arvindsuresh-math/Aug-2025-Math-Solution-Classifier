def solve():
    """Index: 3997.
    Returns: the number of pieces of gum Mitchell chews at once.
    """
    # L1
    num_packets = 8 # 8 packets of gum
    pieces_per_packet = 7 # 7 pieces in each
    total_pieces = num_packets * pieces_per_packet

    # L2
    pieces_not_chewed = 2 # all the gum except for 2 pieces
    pieces_chewed = total_pieces - pieces_not_chewed

    # FA
    answer = pieces_chewed
    return answer