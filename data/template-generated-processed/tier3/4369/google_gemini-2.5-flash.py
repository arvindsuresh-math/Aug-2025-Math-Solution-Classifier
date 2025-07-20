from fractions import Fraction

def solve():
    """Index: 4369.
    Returns: the price Rose paid for the plant after discount.
    """
    # L1
    original_price = 10 # If the price is $10
    discount_percentage = Fraction(10, 100) # 10% discount
    discount_amount = original_price * discount_percentage

    # L2
    final_price = original_price - discount_amount

    # FA
    answer = final_price
    return answer