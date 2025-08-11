def solve():
    """Index: 3590.
    Returns: the number of pages read on the fourth day.
    """
    # L1
    pages_day_one = 63 # 63 pages the first day
    multiplier_day_two = 2 # twice the number of pages
    pages_day_two = pages_day_one * multiplier_day_two

    # L2
    extra_pages_day_three = 10 # 10 mores pages
    pages_day_three = pages_day_two + extra_pages_day_three

    # L3
    total_book_pages = 354 # book is 354 pages long
    pages_day_four = total_book_pages - pages_day_one - pages_day_two - pages_day_three

    # FA
    answer = pages_day_four
    return answer