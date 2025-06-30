def solve_89():
    # Daily average number of books borrowed
    daily_average_books = 40

    # Percentage increase on Friday
    friday_increase_percentage = 40

    # Number of working days in a week (Monday to Friday)
    num_working_days = 5

    # L1: Calculate the extra books borrowed on Friday
    extra_books_on_friday = daily_average_books * (friday_increase_percentage / 100)

    # L2: Calculate the total books borrowed if every day was the average (Monday to Friday)
    # This is the sum of books borrowed on Monday, Tuesday, Wednesday, Thursday, and the base for Friday
    books_borrowed_at_average_rate = daily_average_books * num_working_days

    # L3: Calculate the total books borrowed in a week, including Friday's increase
    total_books_in_week = books_borrowed_at_average_rate + extra_books_on_friday

    return int(total_books_in_week)