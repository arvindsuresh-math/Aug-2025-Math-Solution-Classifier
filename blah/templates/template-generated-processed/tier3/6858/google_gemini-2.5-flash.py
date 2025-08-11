def solve():
    """Index: 6858.
    Returns: the amount by which the final price was lower than the original price.
    """
    # L1
    original_price = 1200 # A luxury perfume costs $1200
    increase_percentage_numerator = 10 # increase its price by 10%
    increase_percentage_denominator = 100 # increase its price by 10%
    price_increase = original_price * increase_percentage_numerator / increase_percentage_denominator

    # L2
    price_after_increase = original_price + price_increase

    # L3
    decrease_percentage_numerator = 15 # lower the price by 15%
    decrease_percentage_denominator = 100 # lower the price by 15%
    price_decrease = price_after_increase * decrease_percentage_numerator / decrease_percentage_denominator

    # L4
    final_price = price_after_increase - price_decrease

    # L5
    price_difference = original_price - final_price

    # FA
    answer = price_difference
    return answer