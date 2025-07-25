from fractions import Fraction

def solve():
    """Index: 6123.
    Returns: the full price of a single green tractor.
    """
    # L1
    red_commission_rate = Fraction(10, 100) # 10% of the sales price
    red_tractor_price = 20000 # The price of a single red tractor is $20,000
    red_commission_per_unit = red_commission_rate * red_tractor_price

    # L2
    num_red_tractors_sold = 2 # sold 2 red tractors
    earnings_from_red_tractors = num_red_tractors_sold * red_commission_per_unit

    # L3
    total_salary = 7000 # Tobias's salary was $7000
    earnings_from_green_tractors = total_salary - earnings_from_red_tractors

    # L4
    num_green_tractors_sold = 3 # sold 3 green tractors
    green_commission_per_unit = earnings_from_green_tractors / num_green_tractors_sold

    # L5
    green_commission_rate_inverse_numerator = 100 # (100/20)
    green_commission_rate_inverse_denominator = 20 # (100/20)
    full_price_green_tractor = (green_commission_rate_inverse_numerator / green_commission_rate_inverse_denominator) * green_commission_per_unit

    # FA
    answer = full_price_green_tractor
    return answer