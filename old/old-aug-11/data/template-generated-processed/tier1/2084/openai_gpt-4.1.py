def solve():
    """Index: 2084.
    Returns: the total number of wheels in the garage.
    """
    # L1
    wheels_per_car = 4 # Each car in the garage has 4 wheels
    num_cars = 2 # 2 car garage, both cars inside
    car_wheels = wheels_per_car * num_cars

    # L2
    lawnmower_wheels = 4 # The riding lawnmower has 4 wheels
    total_after_lawnmower = car_wheels + lawnmower_wheels

    # L3
    wheels_per_bike = 2 # The bicycles have 2 wheels each
    num_bikes = 3 # a bicycle for Timmy as well as each of his parents
    bike_wheels = num_bikes * wheels_per_bike
    total_after_bikes = total_after_lawnmower + bike_wheels

    # L4
    tricycle_wheels = 3 # The tricycle has 3 wheels
    unicycle_wheels = 1 # the unicycle has 1 wheel
    total_wheels = total_after_bikes + unicycle_wheels + tricycle_wheels

    # FA
    answer = total_wheels
    return answer