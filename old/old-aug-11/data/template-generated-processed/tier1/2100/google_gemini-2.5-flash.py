def solve():
    """Index: 2100.
    Returns: the amount of money Victoria should return to her mother.
    """
    # L1
    pizza_cost_per_box = 12 # costs $12 each
    num_pizza_boxes = 2 # bought 2 boxes of pizza
    total_pizza_cost = pizza_cost_per_box * num_pizza_boxes

    # L2
    juice_cost_per_pack = 2 # cost $2 each
    num_juice_packs = 2 # bought 2 packs of juice drinks
    total_juice_cost = juice_cost_per_pack * num_juice_packs

    # L3
    total_paid = total_pizza_cost + total_juice_cost

    # L4
    initial_money = 50 # given a $50 bill
    money_to_return = initial_money - total_paid

    # FA
    answer = money_to_return
    return answer