def solve():
    """Index: 2987.
    Returns: the percentage of comic books Beth owns.
    """
    # L1
    num_graphic_novels = 18 # 18 are graphic novels
    total_books = 120 # 120 books
    proportion_graphic_novels = num_graphic_novels / total_books

    # L2
    percent_multiplier = 100 # WK
    percentage_graphic_novels = percent_multiplier * proportion_graphic_novels

    # L3
    total_percentage = 100 # WK
    novels_percentage = 65 # 65% are novels
    percentage_comic_books = total_percentage - novels_percentage - percentage_graphic_novels

    # FA
    answer = percentage_comic_books
    return answer