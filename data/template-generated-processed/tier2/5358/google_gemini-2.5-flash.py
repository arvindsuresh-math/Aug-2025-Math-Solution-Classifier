def solve():
    """Index: 5358.
    Returns: the total amount of money Kataleya paid for the fruits.
    """
    # L1
    num_peaches = 400 # bought 400 peaches
    cost_per_peach = 0.40 # forty cents each
    total_cost_peaches = num_peaches * cost_per_peach

    # L2
    discount_threshold_amount = 10 # $10 purchase
    num_discount_units = total_cost_peaches / discount_threshold_amount

    # L3
    discount_per_unit = 2 # $2 discount
    total_discount = num_discount_units * discount_per_unit

    # L4
    final_amount_paid = total_cost_peaches - total_discount

    # FA
    answer = final_amount_paid
    return answer