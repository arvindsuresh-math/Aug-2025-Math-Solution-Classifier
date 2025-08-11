def solve():
    """Index: 328.
    Returns: the total number of tires on the used car lot's vehicles.
    """
    # L1
    total_vehicles = 24 # 24 cars and motorcycles (in total)
    motorcycle_fraction_denominator = 3 # A third of the vehicles
    motorcycles = total_vehicles / motorcycle_fraction_denominator
    tires_per_motorcycle = 2 # WK

    # L2
    cars = total_vehicles - motorcycles

    # L3
    spare_tire_fraction_denominator = 4 # a quarter of the cars
    cars_with_spare_tire = cars / spare_tire_fraction_denominator
    tires_per_car_with_spare = 5 # WK

    # L4
    cars_without_spare_tire = cars - cars_with_spare_tire
    tires_per_car_without_spare = 4 # WK

    # L5
    motorcycles_tires_subtotal = motorcycles * tires_per_motorcycle
    cars_with_spare_tires_subtotal = cars_with_spare_tire * tires_per_car_with_spare
    cars_without_spare_tires_subtotal = cars_without_spare_tire * tires_per_car_without_spare
    total_tires = motorcycles_tires_subtotal + cars_with_spare_tires_subtotal + cars_without_spare_tires_subtotal

    # FA
    answer = total_tires
    return answer