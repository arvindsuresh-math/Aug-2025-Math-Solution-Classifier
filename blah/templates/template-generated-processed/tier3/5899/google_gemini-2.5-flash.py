def solve():
    """Index: 5899.
    Returns: the length of each of the shorter sides of the rectangle.
    """
    # L1
    num_longer_sides = 2 # WK
    longer_side_length = 28 # longer sides of the rectangle were 28cm long
    total_length_longer_sides = num_longer_sides * longer_side_length

    # L2
    total_rope_length = 100 # 100cm length of rope he has
    remaining_length_for_short_sides = total_rope_length - total_length_longer_sides

    # L3
    num_short_sides = 2 # WK
    length_of_each_short_side = remaining_length_for_short_sides / num_short_sides

    # FA
    answer = length_of_each_short_side
    return answer