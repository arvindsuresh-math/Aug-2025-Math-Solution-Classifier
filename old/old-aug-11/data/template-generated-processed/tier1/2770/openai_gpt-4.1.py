def solve():
    """Index: 2770.
    Returns: the total amount Robert and Teddy spend in all.
    """
    # L1
    num_pizza_boxes = 5 # five boxes of pizza
    price_per_pizza_box = 10 # $10 each box
    pizza_cost = num_pizza_boxes * price_per_pizza_box

    # L2
    num_soft_drinks_robert = 10 # ten cans of soft drinks
    price_per_soft_drink = 2 # $2 each
    soft_drink_cost_robert = num_soft_drinks_robert * price_per_soft_drink

    # L3
    robert_total = pizza_cost + soft_drink_cost_robert

    # L4
    num_hamburgers = 6 # six hamburgers
    price_per_hamburger = 3 # $3 each
    hamburger_cost = num_hamburgers * price_per_hamburger

    # L5
    num_soft_drinks_teddy = 10 # an additional ten cans of soft drinks
    soft_drink_cost_teddy = num_soft_drinks_teddy * price_per_soft_drink
    teddy_total = hamburger_cost + soft_drink_cost_teddy

    # L6
    total_spent = robert_total + teddy_total

    # FA
    answer = total_spent
    return answer