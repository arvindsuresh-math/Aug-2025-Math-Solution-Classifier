def solve():
    """Index: 328.
    Returns: the total number of tires on the used car lot's vehicles.
    """
    # L1
    total_vehicles = 24 # 24 cars and motorcycles (in total)
    motorcycle_fraction_denominator = 3 # A third of the vehicles are motorcycles
    motorcycles = total_vehicles / motorcycle_fraction_denominator
    motorcycle_tires = 2 # motorcycles with 2 tires each # WK

    # L2
    cars = total_vehicles - motorcycles

    # L3
    spare_tire_fraction_denominator = 4 # a quarter of the cars have a spare tire
    cars_with_spare = cars / spare_tire_fraction_denominator
    tires_per_car_with_spare = 5 # cars with a spare tire have 5 tires each # WK

    # L4
    cars_without_spare = cars - cars_with_spare
    tires_per_car_without_spare = 4 # cars without a spare tire have 4 tires each # WK

    # L5
    total_tires = motorcycles * motorcycle_tires + cars_with_spare * tires_per_car_with_spare + cars_without_spare * tires_per_car_without_spare

    # FA
    answer = total_tires
    return answer