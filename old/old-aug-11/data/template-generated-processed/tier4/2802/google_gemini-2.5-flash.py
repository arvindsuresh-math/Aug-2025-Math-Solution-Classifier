def solve():
    """Index: 2802.
    Returns: the total cost to buy spiral notebooks and personal planners after discount.
    """
    # L1
    notebook_original_price = 15 # A spiral notebook costs $15
    discount_percentage_num = 20 # 20% discount
    percent_divisor = 100 # WK
    discount_factor = 0.2 # WK
    notebook_discount_amount = notebook_original_price * discount_factor

    # L2
    notebook_discounted_price = notebook_original_price - notebook_discount_amount

    # L3
    planner_original_price = 10 # a personal planner costs $10
    planner_discount_amount = (discount_percentage_num / percent_divisor) * planner_original_price

    # L4
    planner_discounted_price = planner_original_price - planner_discount_amount

    # L5
    num_notebooks = 4 # 4 spiral notebooks
    total_notebook_cost = num_notebooks * notebook_discounted_price

    # L6
    num_planners = 8 # 8 personal planners
    total_planner_cost = num_planners * planner_discounted_price

    # L7
    total_cost = total_planner_cost + total_notebook_cost

    # FA
    answer = total_cost
    return answer