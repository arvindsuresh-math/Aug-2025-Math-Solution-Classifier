def solve():
    """Index: 3358.
    Returns: the total amount Bob pays.
    """
    # L1
    total_items = 10 # buys 10 of them
    promotion_factor = 2 # buy one get one free
    items_paid_for = total_items / promotion_factor

    # L2
    cost_per_item = 3 # They each cost $3
    total_cost = items_paid_for * cost_per_item

    # FA
    answer = total_cost
    return answer