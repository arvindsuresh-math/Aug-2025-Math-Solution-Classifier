def solve():
    """Index: 6805.
    Returns: the total cost of the items after discount and cashback.
    """
    # L1
    iphone_price = 800 # an iPhone 12 costs $800
    iphone_discount_numerator = 15 # 15% discount
    percentage_denominator = 100 # 15% discount
    iphone_discount_amount = iphone_price * iphone_discount_numerator / percentage_denominator

    # L2
    iphone_cost_after_discount = iphone_price - iphone_discount_amount

    # L3
    iwatch_price = 300 # an iWatch costs $300
    iwatch_discount_numerator = 10 # 10% discount
    iwatch_discount_amount = iwatch_price * iwatch_discount_numerator / percentage_denominator

    # L4
    iwatch_cost_after_discount = iwatch_price - iwatch_discount_amount

    # L5
    total_cost_before_cashback = iphone_cost_after_discount + iwatch_cost_after_discount

    # L6
    cashback_numerator = 2 # 2% cashback discount
    cashback_amount = total_cost_before_cashback * cashback_numerator / percentage_denominator

    # L7
    final_cost = total_cost_before_cashback - cashback_amount

    # FA
    answer = final_cost
    return answer