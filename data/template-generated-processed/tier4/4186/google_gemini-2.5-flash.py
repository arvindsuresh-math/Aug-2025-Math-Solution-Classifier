def solve():
    """Index: 4186.
    Returns: the average amount John lost.
    """
    # L1
    total_spent = 40 # He spends $40 on loot boxes
    cost_per_box = 5 # loot boxes for $5 each
    num_boxes = total_spent / cost_per_box

    # L2
    average_item_value = 3.5 # The average value of items inside is $3.5
    loss_per_box = cost_per_box - average_item_value

    # L3
    total_loss = loss_per_box * num_boxes

    # FA
    answer = total_loss
    return answer