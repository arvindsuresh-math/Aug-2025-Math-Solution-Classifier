def solve():
    """Index: 195.
    Returns: the amount of change Mary got back after her purchases.
    """
    # L1
    num_drink_boxes = 5 # 5 boxes of drinks
    price_per_drink_box = 6 # $6 each box
    drink_total = num_drink_boxes * price_per_drink_box

    # L2
    num_pizza_boxes = 10 # 10 boxes of pizzas
    price_per_pizza_box = 14 # $14 each box
    pizza_total = num_pizza_boxes * price_per_pizza_box

    # L3
    total_spent = drink_total + pizza_total

    # L4
    total_paid = 200 # She paid $200 for all the items
    change = total_paid - total_spent

    # FA
    answer = change
    return answer