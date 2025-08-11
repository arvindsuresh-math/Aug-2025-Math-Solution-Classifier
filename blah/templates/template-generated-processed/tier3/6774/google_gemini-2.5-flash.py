from fractions import Fraction

def solve():
    """Index: 6774.
    Returns: the number of cars costing between $15000 and $20000.
    """
    # L1
    percentage_less_than_15k = Fraction(15, 100) # 15% of the cars cost less than $15000
    total_cars = 3000 # 3000 cars at the dealership
    cars_less_than_15k = percentage_less_than_15k * total_cars

    # L2
    percentage_more_than_20k = Fraction(40, 100) # 40% of the cars cost more than $20000
    cars_more_than_20k = percentage_more_than_20k * total_cars

    # L3
    cars_outside_range = cars_less_than_15k + cars_more_than_20k

    # L4
    cars_in_range = total_cars - cars_outside_range

    # FA
    answer = cars_in_range
    return answer