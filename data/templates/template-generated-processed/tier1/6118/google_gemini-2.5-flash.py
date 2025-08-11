def solve():
    """Index: 6118.
    Returns: how many more passengers a train with 16 cars can carry than 2 airplanes.
    """
    # L1
    num_train_cars = 16 # 16 cars
    passengers_per_train_car = 60 # 60 passengers
    total_train_passengers = num_train_cars * passengers_per_train_car

    # L2
    num_airplanes = 2 # 2 airplanes
    passengers_per_airplane = 366 # 366 passengers
    total_airplane_passengers = num_airplanes * passengers_per_airplane

    # L3
    difference_in_passengers = total_train_passengers - total_airplane_passengers

    # FA
    answer = difference_in_passengers
    return answer