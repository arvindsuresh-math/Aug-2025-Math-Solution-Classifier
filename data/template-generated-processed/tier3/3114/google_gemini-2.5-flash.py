def solve():
    """Index: 3114.
    Returns: the number of boxes Jill has left to sell to hit her sales goal.
    """
    # L1
    first_customer_boxes = 5 # Her first customer buys 5 boxes
    second_customer_multiplier = 4 # 4 times more than her first customer
    second_customer_boxes = second_customer_multiplier * first_customer_boxes

    # L2
    third_customer_divisor = 2 # half as much as her second
    third_customer_boxes = second_customer_boxes / third_customer_divisor

    # L3
    fourth_customer_multiplier = 3 # 3 times as much as her third
    fourth_customer_boxes = third_customer_boxes * fourth_customer_multiplier

    # L4
    final_customer_boxes = 10 # her final customer buys 10
    total_boxes_sold = first_customer_boxes + final_customer_boxes + second_customer_boxes + third_customer_boxes + fourth_customer_boxes

    # L5
    sales_goal = 150 # she wants to sell at least 150 cookie boxes
    boxes_left_to_sell = sales_goal - total_boxes_sold

    # FA
    answer = boxes_left_to_sell
    return answer