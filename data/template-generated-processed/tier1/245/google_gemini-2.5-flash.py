def solve():
    """Index: 245.
    Returns: the total number of pieces of fruit in the crates and boxes.
    """
    # L1
    num_crates = 12 # 12 crates
    oranges_per_crate = 150 # each contain 150 oranges
    total_oranges = num_crates * oranges_per_crate

    # L2
    num_boxes = 16 # 16 boxes
    nectarines_per_box = 30 # each hold 30 nectarines
    total_nectarines = num_boxes * nectarines_per_box

    # L3
    total_fruit = total_oranges + total_nectarines

    # FA
    answer = total_fruit
    return answer