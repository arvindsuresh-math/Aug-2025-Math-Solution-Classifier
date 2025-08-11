def solve():
    """Index: 195.
    Returns: the amount of change Mary got back.
    """
    # L1
    num_drink_boxes = 5 # 5 boxes of drinks
    cost_per_drink_box = 6 # $6 each box
    cost_of_drinks = num_drink_boxes * cost_per_drink_box

    # L2
    num_pizza_boxes = 10 # 10 boxes of pizzas
    cost_per_pizza_box = 14 # $14 each box
    cost_of_pizzas = num_pizza_boxes * cost_per_pizza_box

    # L3
    total_spent = cost_of_drinks + cost_of_pizzas

    # L4
    amount_paid = 200 # paid $200 for all the items
    change_received = amount_paid - total_spent

    # FA
    answer = change_received
    return answer