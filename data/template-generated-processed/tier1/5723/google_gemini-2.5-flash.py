def solve():
    """Index: 5723.
    Returns: the number of tissues Tucker would have left.
    """
    # L1
    tissues_per_box = 160 # 160 tissues inside a tissue box
    num_boxes = 3 # bought 3 boxes
    total_tissues_bought = tissues_per_box * num_boxes

    # L2
    tissues_used = 210 # used 210 tissues
    tissues_left = total_tissues_bought - tissues_used

    # FA
    answer = tissues_left
    return answer