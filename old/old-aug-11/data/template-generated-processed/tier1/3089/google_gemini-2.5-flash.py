def solve():
    """Index: 3089.
    Returns: the number of books collected in the first week.
    """
    # L2
    total_books_collected = 99 # if she has 99 books now
    multiplier_for_next_weeks = 10 # ten times as many books
    # The implied coefficient of 'x' for the first week's books is 1.
    # The coefficient of 'x' for the next five weeks is the multiplier.
    combined_coefficient_of_x = 1 + multiplier_for_next_weeks

    # L3
    books_first_week = total_books_collected / combined_coefficient_of_x

    # FA
    answer = books_first_week
    return answer