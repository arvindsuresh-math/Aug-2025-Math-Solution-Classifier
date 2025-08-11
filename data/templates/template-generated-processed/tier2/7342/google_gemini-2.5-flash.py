def solve():
    """Index: 7342.
    Returns: the total money saved on shirts.
    """
    # L1
    regular_price_per_shirt = 10 # Any item $10
    first_shirt_discount_percent_text = 0 # 0%
    percent_factor = 0.01 # WK
    first_shirt_discount_amount = first_shirt_discount_percent_text * percent_factor * regular_price_per_shirt

    # L2
    second_shirt_discount_percent_text = 50 # 50% discount
    second_shirt_discount_amount = second_shirt_discount_percent_text * percent_factor * regular_price_per_shirt

    # L3
    third_shirt_discount_percent_text = 60 # 60% discount
    third_shirt_discount_amount = third_shirt_discount_percent_text * percent_factor * regular_price_per_shirt

    # L4
    total_savings = first_shirt_discount_amount + second_shirt_discount_amount + third_shirt_discount_amount

    # FA
    answer = total_savings
    return answer