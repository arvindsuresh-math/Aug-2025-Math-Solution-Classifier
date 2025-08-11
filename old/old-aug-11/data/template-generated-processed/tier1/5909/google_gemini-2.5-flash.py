def solve():
    """Index: 5909.
    Returns: the total number of wheels.
    """
    # L1
    num_cars = 2 # 2 cars in his driveway
    wheels_per_car = 4 # each have 4 wheels
    car_wheels = num_cars * wheels_per_car

    # L2
    num_items_with_2_wheels = 3 # 2 bikes and a trash can
    wheels_per_item_2_wheels = 2 # each have 2 wheels
    bike_trashcan_wheels = num_items_with_2_wheels * wheels_per_item_2_wheels

    # L3
    wheels_per_skate = 4 # Each roller skate has 4 wheels
    num_skates_in_pair = 2 # a pair, which means 2 skates
    roller_skate_wheels = wheels_per_skate * num_skates_in_pair

    # L4
    tricycle_wheels = 3 # 3 wheels on the tricycle
    total_wheels = tricycle_wheels + car_wheels + bike_trashcan_wheels + roller_skate_wheels

    # FA
    answer = total_wheels
    return answer