def solve():
    """Index: 3877.
    Returns: the number of boxes Marissa tied.
    """
    # L1
    total_ribbon_initial = 4.5 # 4.5 feet of ribbon
    ribbon_left = 1 # 1 foot of ribbon is left
    ribbon_used_total = total_ribbon_initial - ribbon_left

    # L2
    ribbon_per_box = 0.7 # 0.7 feet of ribbon to tie each box
    num_boxes = ribbon_used_total / ribbon_per_box

    # FA
    answer = num_boxes
    return answer