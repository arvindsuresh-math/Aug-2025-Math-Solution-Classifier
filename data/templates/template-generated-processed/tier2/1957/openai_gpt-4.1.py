def solve():
    """Index: 1957.
    Returns: the profit John makes from selling the newspapers.
    """
    # L1
    total_newspapers = 500 # John buys 500 newspapers
    sell_percent = 0.8 # He sells 80% of them
    newspapers_sold = total_newspapers * sell_percent

    # L2
    sell_price_per_paper = 2 # Each newspaper sells for $2
    total_revenue = newspapers_sold * sell_price_per_paper

    # L3
    discount_percent = 0.75 # 75% less than the price at which he sells them
    discount_amount = sell_price_per_paper * discount_percent

    # L4
    buy_price_per_paper = sell_price_per_paper - discount_amount

    # L5
    total_cost = total_newspapers * buy_price_per_paper

    # L6
    profit = total_revenue - total_cost

    # FA
    answer = profit
    return answer