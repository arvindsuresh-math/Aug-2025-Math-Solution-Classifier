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
    average_weekly_books = days_open_per_week * average_daily_books # eval: 200 = 5 * 40

    #: L3
    total_books_weekly = average_weekly_books + extra_books_friday # eval: 216.0 = 200 + 16.0

    #: FA
    answer = total_books_weekly # eval: 216.0 = 216.0
    return answer # eval: return 216.0
