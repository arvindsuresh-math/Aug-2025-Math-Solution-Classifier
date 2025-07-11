def solve():
    """Index: 2325.
    Returns: the cost of the Legos set George sold.
    """
    # L1
    num_cars = 3 # sold 3 little cars
    price_per_car = 5 # one little car was sold for $5
    cars_earnings = num_cars * price_per_car

    # L2
    total_earnings = 45 # he earned $45
    legos_cost = total_earnings - cars_earnings

    # FA
    answer = legos_cost
    return answer