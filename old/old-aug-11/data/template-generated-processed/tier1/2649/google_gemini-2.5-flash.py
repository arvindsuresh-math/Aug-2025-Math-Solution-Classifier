def solve():
    """Index: 2649.
    Returns: the total amount Ivan paid.
    """
    # L1
    original_cost = 12 # $12
    discount_per_card = 2 # discount of $2 each
    cost_after_discount = original_cost - discount_per_card

    # L2
    quantity_bought = 10 # ten pieces
    total_paid = cost_after_discount * quantity_bought

    # FA
    answer = total_paid
    return answer