def solve():
    """Index: 2987.
    Returns: the percentage of comic books Beth owns.
    """
    # L1
    num_graphic_novels = 18 # 18 are graphic novels
    total_books = 120 # 120 books
    graphic_novel_proportion = num_graphic_novels / total_books

    # L2
    percent_factor = 100 # WK
    graphic_novel_percent = percent_factor * graphic_novel_proportion

    # L3
    novel_percent = 65 # 65% are novels
    comic_book_percent = percent_factor - novel_percent - graphic_novel_percent

    # FA
    answer = comic_book_percent
    return answer