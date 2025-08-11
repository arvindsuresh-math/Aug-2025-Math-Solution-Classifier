def solve():
    """Index: 4439.
    Returns: the final price of the shirt after profit and discount.
    """
    # L1
    store_buy_price = 20 # The store buys the shirt for $20
    profit_percent = 0.30 # charges 30% for profit
    profit_amount = store_buy_price * profit_percent

    # L2
    regular_selling_price = store_buy_price + profit_amount

    # L3
    sale_discount_percent = 0.50 # on sale for 50% off
    final_price = regular_selling_price * sale_discount_percent

    # FA
    answer = final_price
    return answer