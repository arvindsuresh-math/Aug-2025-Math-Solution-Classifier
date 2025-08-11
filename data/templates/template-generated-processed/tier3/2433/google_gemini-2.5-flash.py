def solve():
    """Index: 2433.
    Returns: the length of the final piece of rope.
    """
    # L1
    initial_rope_length = 100 # Josh has 100 feet of rope
    first_cut_divisor = 2 # cuts the rope in half
    first_half_length = initial_rope_length / first_cut_divisor

    # L2
    second_cut_divisor = 2 # cuts it in half again
    second_half_length = first_half_length / second_cut_divisor

    # L3
    third_cut_divisor = 5 # cuts it into fifths
    final_piece_length = second_half_length / third_cut_divisor

    # FA
    answer = final_piece_length
    return answer