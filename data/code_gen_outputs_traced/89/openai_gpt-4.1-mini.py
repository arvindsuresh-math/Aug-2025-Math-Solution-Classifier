def solve(
    daily_average_books: int = 40,  # borrows an average of 40 books every day
    friday_increase_percent: float = 40,  # Friday's number of borrowed books is about 40% higher
    days_open: int = 5  # library is open from Monday to Friday
):
    """Index: 89.
    Returns: the total number of books Krystian borrows in a week.
    """

    #: L1
    friday_increase_books = daily_average_books * friday_increase_percent / 100 # eval: 16.0 = 40 * 40 / 100

    #: L2
    total_books_mon_to_fri = days_open * daily_average_books # eval: 200 = 5 * 40

    #: L3
    total_books_week = total_books_mon_to_fri + friday_increase_books # eval: 216.0 = 200 + 16.0

    #: FA
    answer = total_books_week
    return answer # eval: return 216.0
