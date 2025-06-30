def solve(
        daily_avg_books: int = 40,  # He borrows an average of 40 books every day
        friday_increase_percentage: float = 0.4,  # Every Friday, his number of borrowed books is about 40% higher
        library_days: int = 5  # library is open from Monday to Friday
    ):
    """Index: 89.
    Returns: the total number of books borrowed in a week."""

    #: L1
    friday_extra_books = daily_avg_books * friday_increase_percentage # eval: 16.0 = 40 * 0.4

    #: L2
    total_books_regular_days = daily_avg_books * library_days # eval: 200 = 40 * 5

    #: L3
    total_books_in_week = total_books_regular_days + friday_extra_books # eval: 216.0 = 200 + 16.0

    #: FA
    answer = total_books_in_week # eval: 216.0 = 216.0
    return answer # eval: return 216.0
