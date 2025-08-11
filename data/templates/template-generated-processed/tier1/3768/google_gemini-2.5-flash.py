def solve():
    """Index: 3768.
    Returns: the total number of washing machines removed from the shipping container.
    """
    # L1
    boxes_per_crate = 6 # 6 boxes
    initial_wm_per_box = 4 # 4 washing machines
    initial_wm_per_crate = boxes_per_crate * initial_wm_per_box

    # L2
    num_crates = 10 # 10 crates
    initial_total_wm = initial_wm_per_crate * num_crates

    # L3
    wm_removed_per_box = 1 # removes 1 washing machine from each box
    current_wm_per_box = initial_wm_per_box - wm_removed_per_box

    # L4
    current_wm_per_crate = boxes_per_crate * current_wm_per_box

    # L5
    current_total_wm = current_wm_per_crate * num_crates

    # L6
    removed_total_wm = initial_total_wm - current_total_wm

    # FA
    answer = removed_total_wm
    return answer