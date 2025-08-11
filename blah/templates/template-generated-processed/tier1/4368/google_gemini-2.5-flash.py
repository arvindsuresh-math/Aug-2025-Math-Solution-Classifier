def solve():
    """Index: 4368.
    Returns: the amount of tape Joy will have left over.
    """
    # L1
    field_width = 20 # 20 feet wide
    field_length = 60 # 60 feet long
    perimeter = field_width + field_width + field_length + field_length

    # L2
    total_tape = 250 # 250 feet of tape
    tape_left_over = total_tape - perimeter

    # FA
    answer = tape_left_over
    return answer