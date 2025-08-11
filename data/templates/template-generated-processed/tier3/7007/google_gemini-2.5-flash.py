def solve():
    """Index: 7007.
    Returns: the number of levels in the tower.
    """
    # L1
    total_pieces = 100 # She has 100 pieces
    pieces_left = 23 # 23 pieces left at the end
    pieces_used = total_pieces - pieces_left

    # L2
    pieces_per_level = 7 # Each level has to be 7 pieces wide
    number_of_levels = pieces_used / pieces_per_level

    # FA
    answer = number_of_levels
    return answer