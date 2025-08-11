from fractions import Fraction

def solve():
    """Index: 658.
    Returns: the difference in price between the two stores.
    """
    # L1
    original_price_store1 = 950 # The first store offers a device for $950
    discount_percentage_numerator_store1 = 6 # with a 6% discount
    discount_percentage_denominator = 100 # 6%
    discount_amount_store1 = original_price_store1 * Fraction(discount_percentage_numerator_store1, discount_percentage_denominator)

    # L2
    price_after_discount_store1 = original_price_store1 - discount_amount_store1

    # L3
    original_price_store2 = 920 # The second sells the same computer for €920
    discount_percentage_numerator_store2 = 5 # with a 5% discount
    discount_amount_store2 = original_price_store2 * Fraction(discount_percentage_numerator_store2, discount_percentage_denominator)

    # L4
    price_after_discount_store2 = original_price_store2 - discount_amount_store2

    # L5
    price_difference = price_after_discount_store1 - price_after_discount_store2

    # FA
    answer = price_difference
    return answer