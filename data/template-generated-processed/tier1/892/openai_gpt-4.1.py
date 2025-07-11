def solve():
    """Index: 892.
    Returns: the amount of discount Clark received.
    """
    # L1
    price_per_part = 80 # part that Clark needs for $80
    num_parts = 7 # buys 7 of them
    original_total = price_per_part * num_parts

    # L2
    amount_paid = 439 # Clark only had to pay $439
    discount = original_total - amount_paid

    # FA
    answer = discount
    return answer