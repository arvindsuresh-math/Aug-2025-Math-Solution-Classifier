def solve():
    """Index: 835.
    Returns: the number of cars that parked in the theater during the play.
    """
    # L1
    cars_front_parking_lot = 100 # 100 cars in the front parking lot
    multiplier_back_lot = 2 # two times more vehicles at the back
    cars_back_parking_lot = cars_front_parking_lot * multiplier_back_lot

    # L2
    total_cars_initial_sum = cars_back_parking_lot + cars_front_parking_lot

    # L3
    total_cars_before_play = total_cars_initial_sum + cars_front_parking_lot

    # L4
    total_cars_end_play = 700 # total number of cars at the end of the play was 700
    cars_parked_during_play = total_cars_end_play - total_cars_before_play

    # FA
    answer = cars_parked_during_play
    return answer