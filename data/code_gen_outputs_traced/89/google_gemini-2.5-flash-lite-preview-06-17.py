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
    books_borrowed_normal_days = avg_books_per_day * (days_open - 1) # eval: 160 = 40 * (5 - 1)

    #: L3
    total_books_borrowed = books_borrowed_normal_days + avg_books_per_day + friday_increase # eval: 216.0 = 160 + 40 + 16.0

    #: FA
    answer = total_books_borrowed # eval: 216.0 = 216.0
    return answer # eval: return 216.0
