def solve():
    """Index: 2743.
    Returns: the amount of money the store has left after the sale.
    """
    # L1
    total_items = 2000 # 2000 different items
    percent_sold = 0.9 # sell 90% of the items
    items_sold = total_items * percent_sold

    # L2
    retail_price = 50 # would normally retail for $50
    discount_percent = 0.8 # offering an 80% discount
    discount_amount = retail_price * discount_percent

    # L3
    sale_price_per_item = retail_price - discount_amount

    # L4
    total_revenue = items_sold * sale_price_per_item

    # L5
    creditors_owed = 15000 # owed $15000 to their creditors
    leftover_money = total_revenue - creditors_owed

    # FA
    answer = leftover_money
    return answer