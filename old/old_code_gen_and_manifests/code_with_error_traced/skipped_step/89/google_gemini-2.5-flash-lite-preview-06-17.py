def solve(
    avg_books_per_day: int = 40, # Krystian borrows an average of 40 books every day
    friday_increase_percentage: float = 0.40, # his number of borrowed books is about 40% higher than the daily average
    days_open: int = 5 # the library is open from Monday to Friday
):
    """Index: 89.
    Returns: the total number of books Krystian borrows in a week.
    """

    #: L1
    friday_increase = avg_books_per_day * friday_increase_percentage # eval: 16.0 = 40 * 0.4

    #: L2

    #: L3
    total_books_borrowed = avg_books_per_day + avg_books_per_day + friday_increase # eval: 96.0 = 40 + 40 + 16.0

    #: FA
    answer = total_books_borrowed
    return answer # eval: return 96.0
