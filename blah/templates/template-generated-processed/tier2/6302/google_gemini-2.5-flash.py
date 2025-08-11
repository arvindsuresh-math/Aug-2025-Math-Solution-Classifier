def solve():
    """Index: 6302.
    Returns: the number of convertibles Pauline owns.
    """
    # L1
    regular_cars_percent = 64 # 64% of them are regular cars
    trucks_percent = 8 # 8% are trucks
    trucks_and_regular_cars_percent = regular_cars_percent + trucks_percent

    # L2
    total_percent = 100 # WK
    convertibles_percent = total_percent - trucks_and_regular_cars_percent

    # L3
    total_cars = 125 # Pauline has 125 matchbox cars
    convertibles_percent_decimal = 0.28 # from solution text: .28
    num_convertibles = total_cars * convertibles_percent_decimal

    # FA
    answer = num_convertibles
    return answer