def solve():
    """Index: 5678.
    Returns: the number of passenger cars in the train.
    """
    # L1
    total_cars_with_engine_caboose = 71 # 71 cars
    engine_caboose_count = 2 # WK
    cars_without_engine_caboose = total_cars_with_engine_caboose - engine_caboose_count

    # L2
    # Let p be the number of passenger cars and c be the number of cargo cars.
    # We know that p + c = cars_without_engine_caboose and c = p/2 + 3
    cargo_cars_half_divisor = 2 # half the number of passenger cars
    cargo_cars_plus_three = 3 # plus three

    # L3
    # Substituting the second equation into the first, we get p + p/cargo_cars_half_divisor + cargo_cars_plus_three = cars_without_engine_caboose

    # L4
    # Combining like terms, we get (1 + 1/cargo_cars_half_divisor)p + cargo_cars_plus_three = cars_without_engine_caboose
    coefficient_p = 1 + (1 / cargo_cars_half_divisor)

    # L5
    # Subtracting cargo_cars_plus_three from both sides, we get coefficient_p * p = cars_without_engine_caboose - cargo_cars_plus_three
    rhs_after_subtraction = cars_without_engine_caboose - cargo_cars_plus_three

    # L6
    # Dividing both sides by coefficient_p, we get p = rhs_after_subtraction / coefficient_p
    passenger_cars = rhs_after_subtraction / coefficient_p

    # FA
    answer = passenger_cars
    return answer