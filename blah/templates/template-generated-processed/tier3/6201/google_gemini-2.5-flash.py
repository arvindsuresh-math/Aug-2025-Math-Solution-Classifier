from fractions import Fraction

def solve():
    """Index: 6201.
    Returns: the percentage of comic books disliked by both males and females.
    """
    # L1
    female_like_percentage = Fraction(30, 100) # 30% are liked by females
    total_comic_books = 300 # 300 comic books
    female_liked_books = female_like_percentage * total_comic_books

    # L2
    male_liked_books = 120 # males like 120
    total_liked_books = female_liked_books + male_liked_books

    # L3
    disliked_books = total_comic_books - total_liked_books

    # L4
    percentage_multiplier = 100 # WK
    disliked_percentage = (disliked_books / total_comic_books) * percentage_multiplier

    # FA
    answer = disliked_percentage
    return answer