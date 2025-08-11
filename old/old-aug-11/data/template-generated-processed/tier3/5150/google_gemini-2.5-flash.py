def solve():
    """Index: 5150.
    Returns: the total amount Paul spent on the two rackets.
    """
    # L1
    full_price = 60 # originally marked at a full price of $60
    half_off_divisor = 2 # half off
    discount_amount = full_price / half_off_divisor

    # L2
    total_spent = full_price + full_price - discount_amount

    # FA
    answer = total_spent
    return answer