def solve():
    """Index: 1714.
    Returns: the total number of boxes in both warehouses combined.
    """
    # L1
    first_warehouse_boxes = 400 # The first warehouse has 400 boxes
    twice_as_many_factor = 2 # twice as many boxes
    second_warehouse_boxes = first_warehouse_boxes / twice_as_many_factor

    # L2
    total_boxes = first_warehouse_boxes + second_warehouse_boxes

    # FA
    answer = total_boxes
    return answer