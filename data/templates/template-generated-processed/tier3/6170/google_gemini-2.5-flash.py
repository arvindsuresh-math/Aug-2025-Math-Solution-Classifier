def solve():
    """Index: 6170.
    Returns: the amount of fuel Lydia can use in the first third of the trip.
    """
    # L1
    total_fuel = 60 # 60 liters of fuel
    second_third_divisor = 3 # a third of all of her fuel
    fuel_second_third = total_fuel / second_third_divisor

    # L2
    half_divisor = 2 # half this amount
    fuel_final_third = fuel_second_third / half_divisor

    # L3
    fuel_first_third = total_fuel - fuel_second_third - fuel_final_third

    # FA
    answer = fuel_first_third
    return answer