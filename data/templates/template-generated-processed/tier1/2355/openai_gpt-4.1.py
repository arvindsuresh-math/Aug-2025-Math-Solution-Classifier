def solve():
    """Index: 2355.
    Returns: the total feet of tape Debbie used to pack and label all boxes.
    """
    # L1
    tape_per_large = 4 # each large box takes 4 feet of packing tape to seal
    num_large = 2 # two large boxes
    tape_large = tape_per_large * num_large

    # L2
    tape_per_medium = 2 # each medium box takes 2 feet of packing tape to seal
    num_medium = 8 # eight medium boxes
    tape_medium = tape_per_medium * num_medium

    # L3
    tape_per_small = 1 # each small box takes 1 foot of packing tape to seal
    num_small = 5 # five small boxes
    tape_small = tape_per_small * num_small

    # L4
    total_boxes = num_large + num_medium + num_small

    # L5
    tape_per_label = 1 # each box also takes 1 foot of packing tape to stick the address label on
    tape_labels = tape_per_label * total_boxes

    # L6
    total_tape = tape_large + tape_medium + tape_small + tape_labels

    # FA
    answer = total_tape
    return answer