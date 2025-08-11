def solve():
    """Index: 2355.
    Returns: the total amount of tape Debbie used.
    """
    # L1
    tape_per_large_box_seal = 4 # Each large box takes 4 feet of packing tape to seal
    num_large_boxes = 2 # two large boxes
    tape_large_boxes_seal = tape_per_large_box_seal * num_large_boxes

    # L2
    tape_per_medium_box_seal = 2 # each medium box takes 2 feet of packing tape to seal
    num_medium_boxes = 8 # eight medium boxes
    tape_medium_boxes_seal = tape_per_medium_box_seal * num_medium_boxes

    # L3
    tape_per_small_box_seal = 1 # each small box takes 1 foot of packing tape to seal
    num_small_boxes = 5 # five small boxes
    tape_small_boxes_seal = tape_per_small_box_seal * num_small_boxes

    # L4
    total_boxes = num_large_boxes + num_medium_boxes + num_small_boxes

    # L5
    tape_per_label = 1 # Each box also takes 1 foot of packing tape to stick the address label on
    tape_for_labels = tape_per_label * total_boxes

    # L6
    total_tape_used = tape_large_boxes_seal + tape_medium_boxes_seal + tape_small_boxes_seal + tape_for_labels

    # FA
    answer = total_tape_used
    return answer