def solve():
    """Index: 3715.
    Returns: the total profit Sam made in dollars.
    """
    # L1
    num_boxes = 12 # a dozen boxes
    cost_per_box = 10 # $10 each box
    total_cost_of_highlighters = num_boxes * cost_per_box

    # L2
    pens_per_box = 30 # 30 highlighter pens inside
    total_highlighters = num_boxes * pens_per_box

    # L3
    num_rearranged_boxes = 5 # five of these boxes
    highlighters_per_rearranged_box = 6 # packages of six highlighters each
    highlighters_from_rearranged_boxes = num_rearranged_boxes * highlighters_per_rearranged_box

    # L4
    price_per_package = 3 # $3 per package
    revenue_from_rearranged_boxes = num_rearranged_boxes * price_per_package

    # L5
    remaining_highlighters = total_highlighters - highlighters_from_rearranged_boxes

    # L6
    pens_per_group_sold_separately = 3 # three pens for $2
    num_groups_sold_separately = remaining_highlighters / pens_per_group_sold_separately

    # L7
    price_per_group_sold_separately = 2 # $2
    revenue_from_separate_sales = num_groups_sold_separately * price_per_group_sold_separately

    # L8
    total_revenue = revenue_from_separate_sales + revenue_from_rearranged_boxes

    # L9
    profit = total_revenue - total_cost_of_highlighters

    # FA
    answer = profit
    return answer