def solve():
    """Index: 432.
    Returns: the total number of people Tina has sold books to.
    """
    # L1
    selling_price_per_book = 20 # $20 for each book she sells
    cost_per_book = 5 # each book costs $5 to make
    profit_per_book = selling_price_per_book - cost_per_book

    # L2
    total_profit = 120 # realizes a $120 profit
    total_books_sold = total_profit / profit_per_book

    # L3
    books_per_customer = 2 # every customer buys 2 at a time
    total_customers = total_books_sold / books_per_customer

    # FA
    answer = total_customers
    return answer