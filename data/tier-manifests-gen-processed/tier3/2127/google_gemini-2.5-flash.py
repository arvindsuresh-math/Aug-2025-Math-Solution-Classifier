from fractions import Fraction

def solve():
    """Index: 2127.
    Returns: the price difference between store A's and store B's smartphones.
    """
    # L1
    store_a_full_price = 125 # full price of $125
    store_a_discount_percentage = Fraction(8, 100) # additional discount of 8%
    store_a_discount_amount = store_a_full_price * store_a_discount_percentage

    # L2
    store_a_final_price = store_a_full_price - store_a_discount_amount

    # L3
    store_b_full_price = 130 # lists the same smartphone for $130
    store_b_discount_percentage = Fraction(10, 100) # additional discount of 10%
    store_b_discount_amount = store_b_full_price * store_b_discount_percentage

    # L4
    store_b_final_price = store_b_full_price - store_b_discount_amount

    # L5
    price_difference = store_b_final_price - store_a_final_price

    # FA
    answer = price_difference
    return answer