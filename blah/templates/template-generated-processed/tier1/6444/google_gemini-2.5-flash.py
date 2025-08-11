def solve():
    """Index: 6444.
    Returns: the number of books that were not sold.
    """
    # L1
    books_sold_monday = 60 # sold 60 on Monday
    books_sold_tuesday = 10 # 10 on Tuesday
    books_sold_wednesday = 20 # 20 on Wednesday
    books_sold_thursday = 44 # 44 on Thursday
    books_sold_friday = 66 # 66 on Friday
    total_books_sold = books_sold_monday + books_sold_tuesday + books_sold_wednesday + books_sold_thursday + books_sold_friday

    # L2
    initial_stock_books = 800 # stock of 800 books
    books_not_sold = initial_stock_books - total_books_sold

    # FA
    answer = books_not_sold
    return answer