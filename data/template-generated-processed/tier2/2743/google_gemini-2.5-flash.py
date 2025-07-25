def solve():
    """Index: 2743.
    Returns: the amount of money left after the sale.
    """
    # L1
    total_items = 2000 # 2000 different items
    items_sold_percent = 0.9 # sell 90% of the items
    items_sold = total_items * items_sold_percent

    # L2
    retail_price = 50 # retail for $50
    discount_rate = 0.8 # offering an 80% discount
    discount_amount_per_item = retail_price * discount_rate

    # L3
    selling_price_per_item = retail_price - discount_amount_per_item

    # L4
    total_revenue = items_sold * selling_price_per_item

    # L5
    creditor_debt = 15000 # owed $15000 to their creditors
    money_left = total_revenue - creditor_debt

    # FA
    answer = money_left
    return answer