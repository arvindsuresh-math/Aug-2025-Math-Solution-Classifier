from fractions import Fraction

def solve():
    """Index: 3303.
    Returns: the total number of empty pages available for her to write on.
    """
    # L1
    total_pages = 500 # a 500 pages book
    pages_written_week1 = 150 # wrote on 150 pages
    empty_pages_after_week1 = total_pages - pages_written_week1

    # L2
    percentage_written_week2 = Fraction(30, 100) # 30% of the remaining pages
    pages_written_week2 = percentage_written_week2 * empty_pages_after_week1

    # L3
    empty_pages_after_week2 = empty_pages_after_week1 - pages_written_week2

    # L4
    percentage_damaged = Fraction(20, 100) # damaged 20 percent of the empty pages
    damaged_pages = percentage_damaged * empty_pages_after_week2

    # L5
    final_empty_pages = empty_pages_after_week2 - damaged_pages

    # FA
    answer = final_empty_pages
    return answer