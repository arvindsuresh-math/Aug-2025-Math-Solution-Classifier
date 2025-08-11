def solve():
    """Index: 7116.
    Returns: the total weight of the remaining chocolate eggs.
    """
    # L1
    total_initial_eggs = 12 # 12 chocolate eggs
    num_gift_boxes = 4 # 4 different gift boxes
    eggs_per_box = total_initial_eggs / num_gift_boxes
    remaining_eggs = total_initial_eggs - eggs_per_box

    # L2
    weight_per_egg = 10 # each weighing 10 ounces
    total_remaining_weight = remaining_eggs * weight_per_egg

    # FA
    answer = total_remaining_weight
    return answer