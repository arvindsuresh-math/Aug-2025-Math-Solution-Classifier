def solve():
    """Index: 2224.
    Returns: the total number of teacups left.
    """
    # L1
    total_attic_boxes = 26 # 26 boxes in her attic
    boxes_of_pans = 6 # 6 of the boxes contain pans
    boxes_decorations_or_teacups = total_attic_boxes - boxes_of_pans

    # L2
    half_divisor = 2 # half of the remaining boxes contain decorations
    boxes_of_teacups = boxes_decorations_or_teacups / half_divisor

    # L3
    rows_per_box = 5 # 5 rows high
    cups_per_row = 4 # 4 cups in each row
    initial_cups_per_box = rows_per_box * cups_per_row

    # L4
    broken_cups_per_box = 2 # breaks 2 of the cups every time he picks up one of the boxes
    remaining_cups_per_box = initial_cups_per_box - broken_cups_per_box

    # L5
    total_teacups_left = boxes_of_teacups * remaining_cups_per_box

    # FA
    answer = total_teacups_left
    return answer