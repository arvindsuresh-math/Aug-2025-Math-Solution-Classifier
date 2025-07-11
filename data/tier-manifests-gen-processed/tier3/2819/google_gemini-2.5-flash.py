def solve():
    """Index: 2819.
    Returns: the total number of chapters Brian read.
    """
    # L1
    num_books_15_chapters = 2 # two books
    chapters_per_book_15 = 15 # 15 chapters each
    chapters_from_15_chapter_books = num_books_15_chapters * chapters_per_book_15

    # L2
    chapters_from_20_chapter_book = 20 # one book that had 20 chapters
    total_chapters_first_three_books = chapters_from_15_chapter_books + chapters_from_20_chapter_book

    # L3
    half_divisor = 2 # half the chapters
    chapters_from_half_book = total_chapters_first_three_books / half_divisor

    # L4
    total_chapters_read = chapters_from_15_chapter_books + chapters_from_20_chapter_book + chapters_from_half_book

    # FA
    answer = total_chapters_read
    return answer