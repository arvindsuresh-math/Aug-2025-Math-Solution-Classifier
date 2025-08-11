def solve():
    """Index: 4102.
    Returns: the original price of the iPhone cases.
    """
    # L1
    total_percentage = 100 # WK
    discount_percentage = 20 # 20%
    price_percentage_after_discount = total_percentage - discount_percentage

    # L2
    paid_amount = 500 # $500
    original_price = (total_percentage / price_percentage_after_discount) * paid_amount

    # FA
    answer = original_price
    return answer