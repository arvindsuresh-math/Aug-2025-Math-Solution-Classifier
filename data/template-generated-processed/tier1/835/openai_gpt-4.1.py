def solve():
    """Index: 835.
    Returns: the number of cars that parked in the theater during the play.
    """
    # L1
    front_cars = 100 # Lana saw 100 cars in the front parking lot
    times_more_back = 2 # two times more vehicles at the back than there were in the front parking lot
    back_cars = front_cars * times_more_back

    # L2
    total_back = back_cars + front_cars

    # L3
    total_before_play = total_back + front_cars

    # L4
    total_end = 700 # total number of cars at the end of the play was 700
    cars_parked_during_play = total_end - total_before_play

    # FA
    answer = cars_parked_during_play
    return answer