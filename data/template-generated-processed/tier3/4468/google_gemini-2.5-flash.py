def solve():
    """Index: 4468.
    Returns: the total profit Owen made.
    """
    # L1
    cost_per_box = 9 # $9 per box
    boxes_bought = 12 # 12 boxes of face masks
    total_cost_boxes = cost_per_box * boxes_bought

    # L2
    boxes_repacked = 6 # repacked 6 of these boxes
    masks_per_box = 50 # Each box has 50 pieces of masks
    masks_in_repacked_boxes = boxes_repacked * masks_per_box

    # L3
    masks_per_repack_sale = 25 # $5 per 25 pieces
    num_repacks = masks_in_repacked_boxes / masks_per_repack_sale

    # L4
    price_per_repack = 5 # $5 per 25 pieces
    revenue_repacked_masks = price_per_repack * num_repacks

    # L5
    remaining_masks = 300 # remaining 300 face masks
    masks_per_baggy_sale = 10 # 10 pieces of mask for $3
    num_baggies = remaining_masks / masks_per_baggy_sale

    # L6
    price_per_baggy = 3 # $3
    revenue_baggies = price_per_baggy * num_baggies

    # L7
    total_revenue = revenue_repacked_masks + revenue_baggies

    # L8
    profit = total_revenue - total_cost_boxes

    # FA
    answer = profit
    return answer