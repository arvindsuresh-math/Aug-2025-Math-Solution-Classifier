def solve():
    """Index: 5396.
    Returns: the total number of pages read after the week is over.
    """
    # L1
    pages_day1 = 10 # He has read 10 pages already on the first day.
    multiplier_for_remaining_days = 2 # reads twice the amount of pages as the first day
    pages_per_day_remaining = pages_day1 * multiplier_for_remaining_days

    # L2
    remaining_days = 6 # remaining 6 days
    total_pages_remaining_days = pages_per_day_remaining * remaining_days

    # L3
    total_pages_week = pages_day1 + total_pages_remaining_days

    # FA
    answer = total_pages_week
    return answer