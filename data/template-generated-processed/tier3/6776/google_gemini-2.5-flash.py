from fractions import Fraction

def solve():
    """Index: 6776.
    Returns: the price difference between the new car and the old car's original price.
    """
    # L1
    new_car_price = 30000 # new $30,000 car
    needed_amount = 4000 # needs only $4,000
    proceeds_from_old_car_sale = new_car_price - needed_amount

    # L2
    sale_percentage = Fraction(80, 100) # 80% of what she originally paid
    original_old_car_price = proceeds_from_old_car_sale / sale_percentage

    # L3
    price_difference = original_old_car_price - new_car_price

    # FA
    answer = price_difference
    return answer