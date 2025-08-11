def solve():
    """Index: 2802.
    Returns: the total cost to buy 4 spiral notebooks and 8 personal planners at a 20% discount.
    """
    # L1
    spiral_notebook_price = 15 # A spiral notebook costs $15
    discount_percent = 20 # 20% discount
    percent_factor = 0.01 # WK
    spiral_discount = discount_percent * percent_factor * spiral_notebook_price

    # L2
    spiral_discounted_price = spiral_notebook_price - spiral_discount

    # L3
    personal_planner_price = 10 # A personal planner costs $10
    planner_discount = discount_percent * percent_factor * personal_planner_price

    # L4
    planner_discounted_price = personal_planner_price - planner_discount

    # L5
    num_spiral_notebooks = 4 # buy 4 spiral notebooks
    total_spiral_cost = num_spiral_notebooks * spiral_discounted_price

    # L6
    num_personal_planners = 8 # buy 8 personal planners
    total_planner_cost = num_personal_planners * planner_discounted_price

    # L7
    total_cost = total_planner_cost + total_spiral_cost

    # FA
    answer = total_cost
    return answer