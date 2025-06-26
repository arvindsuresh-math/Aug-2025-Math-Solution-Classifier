def solve(
    avg_books_per_day: int = 40, # Krystian borrows an average of 40 books every day
    friday_increase_percentage: float = 0.40, # his number of borrowed books is about 40% higher than the daily average
    days_open: int = 5 # the library is open from Monday to Friday
):
    """Index: 89.
    Returns: the total number of books Krystian borrows in a week.
    """

    #: L1
    friday_increase = avg_books_per_day * friday_increase_percentage

    #: L2
    books_borrowed_normal_days = avg_books_per_day * (days_open - 1)

    #: L3
    total_books_borrowed = books_borrowed_normal_days + avg_books_per_day + friday_increase

    answer = total_books_borrowed # FINAL ANSWER
    return answer