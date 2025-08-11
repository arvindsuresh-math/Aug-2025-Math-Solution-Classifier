def solve():
    """Index: 4018.
    Returns: the total amount spent on pizza and soda.
    """
    # L1
    hubert_pizza_boxes = 8 # Hubert orders eight boxes of pizza
    ian_pizza_boxes = 10 # Ian buys ten boxes of pizza
    total_pizza_boxes = hubert_pizza_boxes + ian_pizza_boxes

    # L2
    hubert_soda_cans = 10 # Hubert orders ten cans of soda
    ian_soda_cans = 15 # Ian buys fifteen cans of soda
    total_soda_cans = hubert_soda_cans + ian_soda_cans

    # L3
    cost_per_pizza_box = 14 # One box of pizza is worth $14
    total_pizza_cost = total_pizza_boxes * cost_per_pizza_box

    # L4
    cost_per_soda_can = 1.80 # a can of soda is worth $1.80
    total_soda_cost = total_soda_cans * cost_per_soda_can

    # L5
    total_spend = total_pizza_cost + total_soda_cost

    # FA
    answer = total_spend
    return answer