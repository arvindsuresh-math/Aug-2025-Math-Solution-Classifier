from fractions import Fraction

def solve():
    """Index: 6462.
    Returns: the cost of the book.
    """
    # L1
    cd_discount_percentage = Fraction(30, 100) # 30% cheaper
    album_price = 20 # $20 album
    cd_discount_amount = cd_discount_percentage * album_price

    # L2
    cd_cost = album_price - cd_discount_amount

    # L3
    book_extra_cost = 4 # $4 more than a CD
    book_cost = cd_cost + book_extra_cost

    # FA
    answer = book_cost
    return answer