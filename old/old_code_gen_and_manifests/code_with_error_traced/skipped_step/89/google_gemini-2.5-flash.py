def solve(
        average_daily_books: int = 40, # an average of 40 books every day
        friday_increase_percentage: int = 40, # 40% higher than the daily average
        days_open_per_week: int = 5 # open from Monday to Friday
    ):
    """Index: 89.
    Returns: the total number of books Krystian borrows in a week.
    """

    #: L1
    extra_books_friday = average_daily_books * (friday_increase_percentage / 100) # eval: 16.0 = 40 * (40 / 100)

    #: L2

    #: L3
    total_books_weekly = friday_increase_percentage + extra_books_friday # eval: 56.0 = 40 + 16.0

    #: FA
    answer = total_books_weekly
    return answer # eval: return 56.0
