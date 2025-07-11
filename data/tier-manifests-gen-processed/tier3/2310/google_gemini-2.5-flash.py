def solve():
    """Index: 2310.
    Returns: the number of pages in Harry's book.
    """
    # L1
    selena_pages = 400 # Selena reads a book with 400 pages
    half_divisor = 2 # Half the number of pages
    half_selena_pages = selena_pages / half_divisor

    # L2
    fewer_pages = 20 # 20 fewer than half the number of pages
    harry_pages = half_selena_pages - fewer_pages

    # FA
    answer = harry_pages
    return answer