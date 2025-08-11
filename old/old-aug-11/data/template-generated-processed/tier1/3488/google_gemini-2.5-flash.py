def solve():
    """Index: 3488.
    Returns: the total number of books Evan will have in five years.
    """
    # L1
    books_two_years_ago = 200 # 200 books two years ago
    fewer_books_now = 40 # 40 fewer books than the number he had 2 years ago
    current_books = books_two_years_ago - fewer_books_now

    # L2
    multiplier_five_times = 5 # five times as many books
    five_times_current_books = current_books * multiplier_five_times

    # L3
    additional_books_in_five_years = 60 # 60 more than five times as many books
    total_books_in_five_years = five_times_current_books + additional_books_in_five_years

    # FA
    answer = total_books_in_five_years
    return answer