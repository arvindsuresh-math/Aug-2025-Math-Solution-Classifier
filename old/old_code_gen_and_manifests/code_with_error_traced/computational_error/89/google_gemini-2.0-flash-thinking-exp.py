def solve(
    avg_daily_borrowed: int = 40, # borrows an average of 40 books every day
    friday_increase_percent: int = 40, # his number of borrowed books is about 40% higher than the daily average
    days_in_week: int = 5 # the library is open from Monday to Friday
):
    """Index: 89.
    Returns: the total number of books Krystian borrows in a week.
    """

    #: L1
    friday_increase_books = avg_daily_borrowed * friday_increase_percent / 100 # eval: 16.0 = 40 * 40 / 100

    #: L2
    total_borrowed_avg = days_in_week * avg_daily_borrowed # eval: 200 = 5 * 40

    #: L3
    total_borrowed_week = 206.0 # eval: 206.0 = 206.0

    #: FA
    answer = total_borrowed_week
    return answer # eval: return 206.0
