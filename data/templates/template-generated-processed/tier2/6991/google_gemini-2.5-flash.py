def solve():
    """Index: 6991.
    Returns: the number of pieces left to complete the puzzle.
    """
    # L1
    total_pieces = 1000 # 1000-piece jigsaw puzzle
    first_day_percent = 0.1 # 10% of the pieces
    pieces_first_day = total_pieces * first_day_percent

    # L2
    pieces_remaining_after_first_day = total_pieces - pieces_first_day

    # L3
    second_day_percent = 0.2 # another 20% of the remaining pieces
    pieces_second_day = pieces_remaining_after_first_day * second_day_percent

    # L4
    pieces_remaining_after_second_day = pieces_remaining_after_first_day - pieces_second_day

    # L5
    third_day_percent = 0.3 # 30% of the remaining pieces
    pieces_third_day = pieces_remaining_after_second_day * third_day_percent

    # L6
    pieces_left_final = pieces_remaining_after_second_day - pieces_third_day

    # FA
    answer = pieces_left_final
    return answer