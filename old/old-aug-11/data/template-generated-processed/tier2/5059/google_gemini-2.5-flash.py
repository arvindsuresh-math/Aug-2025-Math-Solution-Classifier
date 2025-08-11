def solve():
    """Index: 5059.
    Returns: how much more money he had compared to before he bought the toys.
    """
    # L1
    buy_price_per_toy = 20 # bought them for $20 each
    total_toys = 200 # had 200 toys
    total_purchase_cost = buy_price_per_toy * total_toys

    # L2
    toys_sold_percent = 0.8 # sell 80% of his toys
    num_toys_sold = total_toys * toys_sold_percent

    # L3
    sell_price_per_toy = 30 # sells them for $30 each
    total_sales_revenue = num_toys_sold * sell_price_per_toy

    # L4
    profit = total_sales_revenue - total_purchase_cost

    # FA
    answer = profit
    return answer