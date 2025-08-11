def solve():
    """Index: 1957.
    Returns: the profit John makes.
    """
    # L1
    total_newspapers = 500 # John buys 500 newspapers
    sell_percentage = 0.8 # sells 80% of them
    newspapers_sold = total_newspapers * sell_percentage

    # L2
    sell_price_per_newspaper = 2 # Each newspaper sells for $2
    total_revenue = newspapers_sold * sell_price_per_newspaper

    # L3
    buy_discount_percentage = 0.75 # 75% less than the price at which he sells them
    discount_amount_per_newspaper = sell_price_per_newspaper * buy_discount_percentage

    # L4
    buy_price_per_newspaper = sell_price_per_newspaper - discount_amount_per_newspaper

    # L5
    total_cost = total_newspapers * buy_price_per_newspaper

    # L6
    profit = total_revenue - total_cost

    # FA
    answer = profit
    return answer