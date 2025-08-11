def solve():
    """Index: 730.
    Returns: the amount of money Jack lost.
    """
    # L1
    books_per_month = 3 # 3 books a month
    cost_per_book = 20 # $20 each
    cost_per_month = books_per_month * cost_per_book

    # L2
    months_per_year = 12 # WK
    cost_per_year = cost_per_month * months_per_year

    # L3
    selling_price = 500 # $500
    money_lost = cost_per_year - selling_price

    # FA
    answer = money_lost
    return answer