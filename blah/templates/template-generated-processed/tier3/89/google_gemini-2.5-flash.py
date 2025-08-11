from fractions import Fraction

def solve():
    """Index: 89.
    Returns: the total number of books Krystian borrows in a week.
    """
    # L1
    daily_average_books = 40 # an average of 40 books every day
    friday_increase_percentage = Fraction(40, 100) # about 40% higher
    friday_additional_books = daily_average_books * friday_increase_percentage

    # L2
    working_days_per_week = 5 # from Monday to Friday
    average_weekly_books = working_days_per_week * daily_average_books

    # L3
    total_weekly_books = average_weekly_books + friday_additional_books

    # FA
    answer = total_weekly_books
    return answer