def solve():
    """Index: 937.
    Returns: the final cost of the dress after the discount.
    """
    # L1
    dress_price = 50 # the dress she wanted was $50
    discount_percent_decimal = 0.30 # 30% off
    discount_amount = dress_price * discount_percent_decimal

    # L2
    final_cost = dress_price - discount_amount

    # FA
    answer = final_cost
    return answer