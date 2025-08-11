def solve():
    """Index: 2936.
    Returns: the number of black cars in the parking lot.
    """
    # L1
    total_cars = 516 # 516 cars in a parking lot
    blue_fraction_numerator = 1 # One-third are blue
    blue_fraction_denominator = 3 # One-third are blue
    blue_cars = total_cars * (blue_fraction_numerator / blue_fraction_denominator)

    # L2
    red_fraction_numerator = 1 # one-half are red
    red_fraction_denominator = 2 # one-half are red
    red_cars = total_cars * (red_fraction_numerator / red_fraction_denominator)

    # L3
    black_cars = total_cars - (blue_cars + red_cars)

    # FA
    answer = black_cars
    return answer