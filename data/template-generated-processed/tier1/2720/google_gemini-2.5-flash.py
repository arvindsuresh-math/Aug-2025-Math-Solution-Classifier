def solve():
    """Index: 2720.
    Returns: the number of additional boxes Kaylee needs to sell.
    """
    # L1
    lemon_boxes_sold = 12 # sold 12 boxes of lemon biscuits
    chocolate_boxes_sold = 5 # sold 5 boxes of chocolate biscuits
    oatmeal_boxes_sold = 4 # sold 4 boxes of oatmeal biscuits
    total_boxes_sold = lemon_boxes_sold + chocolate_boxes_sold + oatmeal_boxes_sold

    # L2
    total_boxes_needed = 33 # needs to sell 33 boxes of biscuits
    boxes_remaining_to_sell = total_boxes_needed - total_boxes_sold

    # FA
    answer = boxes_remaining_to_sell
    return answer