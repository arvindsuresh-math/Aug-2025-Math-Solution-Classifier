def solve():
    """Index: 4726.
    Returns: the total number of books Matias sold during these three days combined.
    """
    # L1
    books_tuesday = 7 # sold 7 books on Tuesday
    multiplier_wednesday = 3 # three times as many on Wednesday
    books_wednesday = books_tuesday * multiplier_wednesday

    # L2
    multiplier_thursday = 3 # sales from Wednesday were tripled on Thursday
    books_thursday = books_wednesday * multiplier_thursday

    # L3
    total_books_sold = books_tuesday + books_wednesday + books_thursday

    # FA
    answer = total_books_sold
    return answer