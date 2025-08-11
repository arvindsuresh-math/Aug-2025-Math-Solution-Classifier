from fractions import Fraction

def solve():
    """Index: 5465.
    Returns: the final price Donald will pay for the laptop.
    """
    # L1
    original_price = 800 # laptop originally costs $800
    discount_percentage_numerator = 15 # 15% reduction
    discount_percentage_denominator = 100 # 15% reduction
    discount_amount = original_price * Fraction(discount_percentage_numerator, discount_percentage_denominator)

    # L2
    final_price = original_price - discount_amount

    # FA
    answer = final_price
    return answer