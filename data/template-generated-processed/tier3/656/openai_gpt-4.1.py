def solve():
    """Index: 656.
    Returns: the total number of books Zig and Flo wrote altogether.
    """
    # L1
    zig_books = 60 # Zig wrote 60 books
    zig_to_flo_ratio = 4 # four times as many books as Flo
    flo_books = zig_books / zig_to_flo_ratio

    # L2
    total_books = zig_books + flo_books

    # FA
    answer = total_books
    return answer