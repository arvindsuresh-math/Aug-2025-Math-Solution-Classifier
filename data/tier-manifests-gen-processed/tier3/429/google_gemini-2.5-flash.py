from fractions import Fraction

def solve():
    """Index: 429.
    Returns: the number of English-language books published outside the country.
    """
    # L1
    english_percentage = Fraction(80, 100) # 80% of all the books are in English
    total_books = 2300 # 2300 different books
    english_books = english_percentage * total_books

    # L2
    published_in_country_percentage = Fraction(60, 100) # only 60% of these books were published in the country
    english_books_published_in_country = published_in_country_percentage * english_books

    # L3
    english_books_published_outside_country = english_books - english_books_published_in_country

    # FA
    answer = english_books_published_outside_country
    return answer