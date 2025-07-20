def solve():
    """Index: 5214.
    Returns: the current number of dogs Derek has.
    """
    # L1
    initial_dogs = 90 # he had 90 dogs when he was six years old
    dogs_to_cars_ratio = 3 # three times as many dogs as cars
    initial_cars = initial_dogs / dogs_to_cars_ratio

    # L2
    cars_bought_later = 210 # buying 210 more cars
    current_cars = cars_bought_later + initial_cars

    # L3
    cars_to_dogs_ratio = 2 # the number of cars became twice the number of dogs
    current_dogs = current_cars / cars_to_dogs_ratio

    # FA
    answer = current_dogs
    return answer