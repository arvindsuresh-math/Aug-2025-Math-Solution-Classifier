def solve():
    """Index: 2325.
    Returns: the cost of the Legos set.
    """
    # L1
    num_cars_sold = 3 # 3 little cars
    price_per_car = 5 # one little car was sold for $5
    earnings_from_cars = num_cars_sold * price_per_car

    # L2
    total_earned = 45 # In total, he earned $45
    lego_set_cost = total_earned - earnings_from_cars

    # FA
    answer = lego_set_cost
    return answer