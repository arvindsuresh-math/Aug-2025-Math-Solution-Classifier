from fractions import Fraction

def solve():
    """Index: 1530.
    Returns: the total number of pages Miles reads.
    """
    # L1
    reading_fraction_of_day = Fraction(1, 6) # 1/6 of a day reading
    hours_per_day = 24 # WK
    total_reading_hours = hours_per_day * reading_fraction_of_day

    # L2
    number_of_types = 3 # comic books, graphic novels, and novels
    hours_per_type = total_reading_hours / number_of_types

    # L3
    novel_pages_per_hour = 21 # 21 pages an hour when he reads novels
    novel_pages_read = novel_pages_per_hour * hours_per_type

    # L4
    graphic_novel_pages_per_hour = 30 # 30 pages an hour when he reads graphic novels
    graphic_novel_pages_read = graphic_novel_pages_per_hour * hours_per_type

    # L5
    comic_book_pages_per_hour = 45 # 45 pages an hour when he reads comic books
    comic_book_pages_read = comic_book_pages_per_hour * hours_per_type

    # L6
    total_pages_read = novel_pages_read + graphic_novel_pages_read + comic_book_pages_read

    # FA
    answer = total_pages_read
    return answer