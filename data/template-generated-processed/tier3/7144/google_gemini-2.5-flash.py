from fractions import Fraction

def solve():
    """Index: 7144.
    Returns: the price of the iPhone after the second month.
    """
    # L1
    first_month_percentage_fall = Fraction(10, 100) # fell 10%
    initial_price = 1000 # initial price was $1000
    price_fall_first_month = first_month_percentage_fall * initial_price

    # L2
    price_after_first_month = initial_price - price_fall_first_month

    # L3
    second_month_percentage_fall = Fraction(20, 100) # another 20%
    price_fall_second_month = second_month_percentage_fall * price_after_first_month

    # L4
    final_price = price_after_first_month - price_fall_second_month

    # FA
    answer = final_price
    return answer