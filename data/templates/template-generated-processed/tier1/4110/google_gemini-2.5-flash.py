def solve():
    """Index: 4110.
    Returns: the amount Michael paid to the seller.
    """
    # L1
    suit_cost = 430 # suit for $430
    shoes_cost = 190 # shoes for $190
    amount_before_deduction = suit_cost + shoes_cost

    # L2
    discount_amount = 100 # $100 discount
    amount_paid = amount_before_deduction - discount_amount

    # FA
    answer = amount_paid
    return answer