def solve():
    """Index: 5601.
    Returns: the original price of the shirt.
    """
    # L2
    total_percent = 100 # WK
    remaining_percent = 25 # This price is at 25% of the original price
    discount_percent = total_percent - remaining_percent

    # L3
    full_price_factor = 1.0 # WK
    discount_decimal = 0.75 # from solution text: .75x
    sale_price_factor = full_price_factor - discount_decimal

    # L4
    sale_price = 6 # reduced to $6
    original_price = sale_price / sale_price_factor

    # FA
    answer = original_price
    return answer