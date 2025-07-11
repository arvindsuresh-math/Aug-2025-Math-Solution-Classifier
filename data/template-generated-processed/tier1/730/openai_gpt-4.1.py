def solve():
    """Index: 730.
    Returns: the amount of money Jack lost.
    """
    # L1
    books_per_month = 3 # 3 books a month
    price_per_book = 20 # $20 each
    monthly_spending = books_per_month * price_per_book

    # L2
    months_in_year = 12 # WK
    yearly_spending = monthly_spending * months_in_year

    # L3
    resale_value = 500 # sells them back at the end of the year for $500
    money_lost = yearly_spending - resale_value

    # FA
    answer = money_lost
    return answer