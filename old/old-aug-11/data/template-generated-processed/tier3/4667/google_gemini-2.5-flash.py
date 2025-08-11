def solve():
    """Index: 4667.
    Returns: the length of each of the equal pieces in millimeters.
    """
    # L1
    total_rope_length_cm = 1165 # A 1165 cm long rope
    mm_per_cm = 10 # WK
    total_rope_length_mm = total_rope_length_cm * mm_per_cm

    # L2
    total_pieces = 154 # cut into 154 pieces
    equal_pieces_count = 150 # 150 of the pieces are equally sized
    unequal_pieces_count = total_pieces - equal_pieces_count

    # L3
    length_of_unequal_piece_mm = 100 # the remaining pieces are 100mm each
    total_length_of_unequal_pieces = unequal_pieces_count * length_of_unequal_piece_mm

    # L4
    remaining_length_for_equal_pieces = total_rope_length_mm - total_length_of_unequal_pieces

    # L5
    length_of_each_equal_piece_mm = remaining_length_for_equal_pieces / equal_pieces_count

    # FA
    answer = length_of_each_equal_piece_mm
    return answer