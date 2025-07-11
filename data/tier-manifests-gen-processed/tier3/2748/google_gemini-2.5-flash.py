from fractions import Fraction

def solve():
    """Index: 2748.
    Returns: the final price of the book.
    """
    # L1
    decrease_percentage = Fraction(15, 100) # decreased by 15%
    initial_price = 400 # The price of a book was $400
    price_decrease_amount = decrease_percentage * initial_price

    # L2
    price_after_decrease = initial_price - price_decrease_amount

    # L3
    increase_percentage = Fraction(40, 100) # increased by 40%
    price_increase_amount = increase_percentage * price_after_decrease

    # L4
    final_price = price_after_decrease + price_increase_amount

    # FA
    answer = final_price
    return answer