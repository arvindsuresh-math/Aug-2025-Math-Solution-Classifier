from fractions import Fraction

def solve():
    """Index: 89.
    Returns: the total number of books Krystian borrows in a week (Monday to Friday).
    """
    # L1
    daily_average = 40 # borrows an average of 40 books every day
    friday_increase_percent = 40 # 40% higher than the daily average
    percent_divisor = 100 # WK
    friday_increase = daily_average * Fraction(friday_increase_percent, percent_divisor)

    # L2
    days_open = 5 # library is open from Monday to Friday
    total_books_without_friday_increase = days_open * daily_average

    # L3
    total_books_week = total_books_without_friday_increase + friday_increase

    # FA
    answer = total_books_week
    return answer