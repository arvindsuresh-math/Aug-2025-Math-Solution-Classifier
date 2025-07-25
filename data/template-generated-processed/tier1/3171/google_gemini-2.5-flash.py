def solve():
    """Index: 3171.
    Returns: the total amount of tape Brian needs.
    """
    # L1
    num_short_sides_per_box = 2 # two as long as the short side
    short_side_length_box1 = 15 # 15 inches by 30 inches
    tape_for_short_sides_box1 = num_short_sides_per_box * short_side_length_box1

    # L2
    long_side_length_box1 = 30 # 15 inches by 30 inches
    total_tape_per_box1 = tape_for_short_sides_box1 + long_side_length_box1

    # L3
    num_boxes1 = 5 # 5 boxes that measure 15 inches by 30 inches
    total_tape_for_box1_type = total_tape_per_box1 * num_boxes1

    # L4
    num_sides_square_box = 3 # three pieces of tape
    side_length_square_box = 40 # 40 inches square
    total_tape_per_box2 = num_sides_square_box * side_length_square_box

    # L5
    num_boxes2 = 2 # 2 boxes that measure 40 inches square
    total_tape_for_box2_type = total_tape_per_box2 * num_boxes2

    # L6
    grand_total_tape = total_tape_for_box2_type + total_tape_for_box1_type

    # FA
    answer = grand_total_tape
    return answer