def solve():
    """Index: 14.
    Returns: the number of hours it will take Joy to read 120 pages.
    """
    # L2
    pages_per_20min = 8 # Joy can read 8 pages of a book in 20 minutes
    sets_per_hour = 3 # In one hour, there are 3 sets of 20 minutes
    pages_per_hour = pages_per_20min * sets_per_hour

    # L3
    total_pages = 120 # How many hours will it take her to read 120 pages?
    hours_needed = total_pages / pages_per_hour

    # FA
    answer = hours_needed
    return answer