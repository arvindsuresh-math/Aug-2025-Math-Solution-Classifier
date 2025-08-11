def solve():
    """Index: 2084.
    Returns: the total number of wheels in the garage.
    """
    # L1
    num_cars = 2 # 2 car garage
    wheels_per_car = 4 # WK
    car_wheels_total = wheels_per_car * num_cars

    # L2
    wheels_lawnmower = 4 # The riding lawnmower has 4 wheels
    current_total_after_lawnmower = car_wheels_total + wheels_lawnmower

    # L3
    num_bicycles = 3 # a bicycle for Timmy as well as each of his parents
    wheels_per_bicycle = 2 # WK
    bicycle_wheels_total = num_bicycles * wheels_per_bicycle
    current_total_after_bicycles = current_total_after_lawnmower + bicycle_wheels_total

    # L4
    wheels_per_tricycle = 3 # The tricycle has 3 wheels
    wheels_per_unicycle = 1 # the unicycle has 1 wheel
    final_total_wheels = current_total_after_bicycles + wheels_per_unicycle + wheels_per_tricycle

    # FA
    answer = final_total_wheels
    return answer