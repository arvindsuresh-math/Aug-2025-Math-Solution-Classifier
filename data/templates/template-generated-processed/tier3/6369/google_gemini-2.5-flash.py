def solve():
    """Index: 6369.
    Returns: the length of each final piece of rope.
    """
    # L1
    total_rope_length = 200 # A rope has a length of 200 meters
    num_initial_parts = 4 # cuts the rope into four equal parts
    length_of_each_initial_piece = total_rope_length / num_initial_parts

    # L2
    subdivision_factor = 2 # subdivides the remaining pieces into two more equal parts
    final_piece_length = length_of_each_initial_piece / subdivision_factor

    # FA
    answer = final_piece_length
    return answer