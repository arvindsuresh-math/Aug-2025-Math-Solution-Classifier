def solve():
    """Index: 3594.
    Returns: the original price of the dining table.
    """
    # L1
    total_percentage = 100 # WK
    discount_percentage = 10 # a 10% discount
    percentage_paid = total_percentage - discount_percentage

    # L2
    sale_price = 450 # paid the sale price of $450
    value_per_percent = sale_price / percentage_paid

    # L3
    total_percentage_for_original_price = 100 # WK
    original_price = value_per_percent * total_percentage_for_original_price

    # FA
    answer = original_price
    return answer