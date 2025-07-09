def solve(
    daily_average_books: int = 40,  # Krystian borrows an average of 40 books every day
    friday_increase_percent: float = 40,  # Every Friday, his number of borrowed books is about 40% higher
    days_open: int = 5  # library is open from Monday to Friday
):
    """Index: 89.
    Returns: the total number of books Krystian borrows in a week.
    """
    #: L1
    friday_increase = daily_average_books * friday_increase_percent / 100

    #: L2
    total_books_without_friday_increase = daily_average_books * days_open

    #: L3
    total_books_with_friday_increase = total_books_without_friday_increase + friday_increase

    answer = total_books_with_friday_increase  # FINAL ANSWER
    return answer