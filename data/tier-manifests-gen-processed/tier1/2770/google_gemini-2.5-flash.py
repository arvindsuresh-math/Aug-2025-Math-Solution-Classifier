def solve():
    """Index: 2770.
    Returns: the total amount Robert and Teddy spend in all.
    """
    # L1
    num_pizza_boxes = 5 # five boxes of pizza
    cost_per_pizza_box = 10 # $10 each box
    cost_pizza = num_pizza_boxes * cost_per_pizza_box

    # L2
    num_soft_drinks_robert = 10 # ten cans of soft drinks
    cost_per_soft_drink = 2 # $2 each
    cost_soft_drinks_robert = num_soft_drinks_robert * cost_per_soft_drink

    # L3
    total_robert_spend = cost_pizza + cost_soft_drinks_robert

    # L4
    num_hamburgers = 6 # six hamburgers
    cost_per_hamburger = 3 # $3 each
    cost_hamburgers = num_hamburgers * cost_per_hamburger

    # L5
    num_soft_drinks_teddy = 10 # an additional ten cans of soft drinks
    cost_soft_drinks_teddy = num_soft_drinks_teddy * cost_per_soft_drink
    total_teddy_spend = cost_hamburgers + cost_soft_drinks_teddy

    # L6
    total_spend = total_robert_spend + total_teddy_spend

    # FA
    answer = total_spend
    return answer