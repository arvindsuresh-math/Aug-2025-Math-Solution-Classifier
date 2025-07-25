def solve():
    """Index: 1820.
    Returns: the number of additional boxes needed.
    """
    # L1
    total_chocolates = 50 # Nida has 50 chocolates
    chocolates_not_in_box = 5 # 5 pieces are not in a box
    chocolates_in_boxes = total_chocolates - chocolates_not_in_box

    # L2
    initial_filled_boxes = 3 # 3 filled boxes
    chocolates_per_box = chocolates_in_boxes / initial_filled_boxes

    # L3
    chocolates_from_friend = 25 # Her friend brought 25 pieces of chocolates
    chocolates_to_box = chocolates_not_in_box + chocolates_from_friend

    # L4
    boxes_needed = chocolates_to_box / chocolates_per_box

    # FA
    answer = boxes_needed
    return answer