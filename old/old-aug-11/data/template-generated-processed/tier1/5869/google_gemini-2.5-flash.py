def solve():
    """Index: 5869.
    Returns: the number of toy cars Jaden has left.
    """
    # L1
    initial_cars = 14 # 14 toy cars
    bought_cars = 28 # bought 28 cars from the toy store
    cars_after_buying = initial_cars + bought_cars

    # L2
    birthday_cars = 12 # got 12 cars for his birthday
    cars_after_birthday = cars_after_buying + birthday_cars

    # L3
    given_to_sister = 8 # gave 8 of the toy cars to his sister
    cars_after_sister = cars_after_birthday - given_to_sister

    # L4
    given_to_vinnie = 3 # 3 to his friend Vinnie
    cars_left = cars_after_sister - given_to_vinnie

    # FA
    answer = cars_left
    return answer