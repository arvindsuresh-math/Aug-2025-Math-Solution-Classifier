def solve():
    """Index: 552.
    Returns: the number of cars that can be parked in the lot.
    """
    # L1
    lot_length = 400 # 400 feet
    lot_width = 500 # 500 feet
    lot_area = lot_length * lot_width

    # L2
    usable_percent = 0.8 # 80% of that is useable for parking
    usable_area = lot_area * usable_percent

    # L3
    area_per_car = 10 # 10 square feet to park a car
    num_cars = usable_area / area_per_car

    # FA
    answer = num_cars
    return answer