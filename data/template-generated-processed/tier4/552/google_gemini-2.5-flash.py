def solve():
    """Index: 552.
    Returns: the number of cars that can be parked.
    """
    # L1
    length_ft = 400 # 400 feet
    width_ft = 500 # 500 feet
    total_area_sq_ft = length_ft * width_ft

    # L2
    usable_percent = 0.8 # 80% of that is useable
    usable_area_sq_ft = total_area_sq_ft * usable_percent

    # L3
    area_per_car_sq_ft = 10 # 10 square feet to park a car
    num_cars = usable_area_sq_ft / area_per_car_sq_ft

    # FA
    answer = num_cars
    return answer