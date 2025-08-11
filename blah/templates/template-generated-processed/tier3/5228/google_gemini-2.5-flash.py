def solve():
    """Index: 5228.
    Returns: the total number of boxes of apples.
    """
    # L1
    apples_per_crate = 42 # 42 apples in a crate
    crates_delivered = 12 # 12 crates of apples were delivered
    total_apples_delivered = apples_per_crate * crates_delivered

    # L2
    rotten_apples = 4 # 4 apples were rotten
    remaining_apples = total_apples_delivered - rotten_apples

    # L3
    apples_per_box = 10 # boxes that could fit 10 apples each
    number_of_boxes = remaining_apples / apples_per_box

    # FA
    answer = number_of_boxes
    return answer