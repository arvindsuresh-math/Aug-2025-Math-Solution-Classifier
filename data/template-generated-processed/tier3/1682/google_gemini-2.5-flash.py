def solve():
    """Index: 1682.
    Returns: the total money John has made writing.
    """
    # L1
    months_per_year = 12 # WK
    months_per_book = 2 # every 2 months
    books_per_year = months_per_year / months_per_book

    # L2
    writing_years = 20 # for 20 years
    total_books_written = books_per_year * writing_years

    # L3
    earnings_per_book = 30000 # earned an average of $30,000 per book
    total_money_made = total_books_written * earnings_per_book

    # FA
    answer = total_money_made
    return answer