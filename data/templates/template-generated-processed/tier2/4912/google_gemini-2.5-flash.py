def solve():
    """Index: 4912.
    Returns: the number of pages Joey must read after he takes a break.
    """
    # L1
    total_pages = 30 # 30 pages to read
    break_percent_decimal = 0.7 # 70% of the pages assigned
    pages_before_break = total_pages * break_percent_decimal

    # L2
    pages_after_break = total_pages - pages_before_break

    # FA
    answer = pages_after_break
    return answer