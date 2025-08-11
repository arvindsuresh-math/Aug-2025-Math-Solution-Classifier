def solve():
    """Index: 4512.
    Returns: the total money Vincent will earn after five days.
    """
    # L1
    fantasy_book_price = 4 # fantasy books cost $4 each
    fantasy_books_sold_per_day = 5 # sold five fantasy books
    daily_fantasy_earnings = fantasy_book_price * fantasy_books_sold_per_day

    # L2
    literature_price_divisor = 2 # half of the price
    literature_book_price = fantasy_book_price / literature_price_divisor

    # L3
    literature_books_sold_per_day = 8 # eight literature books per day
    daily_literature_earnings = literature_book_price * literature_books_sold_per_day

    # L4
    total_daily_earnings = daily_literature_earnings + daily_fantasy_earnings

    # L5
    number_of_days = 5 # after five days
    total_earnings_five_days = total_daily_earnings * number_of_days

    # FA
    answer = total_earnings_five_days
    return answer