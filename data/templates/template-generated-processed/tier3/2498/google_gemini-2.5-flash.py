def solve():
    """Index: 2498.
    Returns: the total cost Mark paid for the chicken nuggets.
    """
    # L1
    total_nuggets_ordered = 100 # Mark orders 100 chicken nuggets
    nuggets_per_box = 20 # A 20 box of chicken nuggets
    num_boxes = total_nuggets_ordered / nuggets_per_box

    # L2
    cost_per_box = 4 # cost $4
    total_cost = num_boxes * cost_per_box

    # FA
    answer = total_cost
    return answer