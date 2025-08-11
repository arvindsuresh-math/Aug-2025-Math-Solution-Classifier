from fractions import Fraction

def solve():
    """Index: 6364.
    Returns: the total sum of money Toby made at the garage sale.
    """
    # L1
    treadmill_price = 100 # sold a treadmill for $100
    half_divisor = 2 # half as much
    chest_of_drawers_price = treadmill_price / half_divisor

    # L2
    three_times_multiplier = 3 # three times
    television_price = treadmill_price * three_times_multiplier

    # L3
    three_items_total = treadmill_price + chest_of_drawers_price + television_price

    # L4
    percentage_of_total = Fraction(75, 100) # 75% of the total amount of sales money
    total_sales_money = three_items_total / percentage_of_total

    # FA
    answer = total_sales_money
    return answer