def solve():
    """Index: 6626.
    Returns: the total number of sheets of paper used.
    """
    # L1
    pages_per_book = 600 # each 600 pages long
    num_books = 2 # 2 books
    total_pages_printed = pages_per_book * num_books

    # L2
    pages_per_side = 4 # 4 pages per side
    sides_per_sheet = 2 # double-sided
    pages_per_sheet = pages_per_side * sides_per_sheet

    # L3
    sheets_of_paper_used = total_pages_printed / pages_per_sheet

    # FA
    answer = sheets_of_paper_used
    return answer