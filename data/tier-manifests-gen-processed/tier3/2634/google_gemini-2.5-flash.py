from fractions import Fraction

def solve():
    """Index: 2634.
    Returns: the amount Peter can save by buying from other bookshops.
    """
    # L1
    discount_percentage = Fraction(20, 100) # 20% less
    school_price_per_book = 45 # The price of a math textbook in the school bookshop is $45
    discount_amount = discount_percentage * school_price_per_book

    # L2
    other_bookshop_price_per_book = school_price_per_book - discount_amount

    # L3
    number_of_textbooks = 3 # he wants to buy 3 math textbooks
    total_cost_school = school_price_per_book * number_of_textbooks

    # L4
    total_cost_other_bookshop = other_bookshop_price_per_book * number_of_textbooks

    # L5
    savings = total_cost_school - total_cost_other_bookshop

    # FA
    answer = savings
    return answer