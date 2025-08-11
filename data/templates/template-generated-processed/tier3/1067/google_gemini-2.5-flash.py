def solve():
    """Index: 1067.
    Returns: the total number of boxes of apples.
    """
    # L1
    apples_per_crate = 180 # 180 apples in each crate
    num_crates = 12 # 12 such crates of apples
    total_apples_delivered = apples_per_crate * num_crates

    # L2
    rotten_apples = 160 # 160 apples were rotten
    remaining_apples = total_apples_delivered - rotten_apples

    # L3
    apples_per_box = 20 # boxes of 20 apples each
    total_boxes = remaining_apples / apples_per_box

    # FA
    answer = total_boxes
    return answer