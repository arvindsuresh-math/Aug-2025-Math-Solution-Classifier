from fractions import Fraction

def solve():
    """Index: 5834.
    Returns: the number of parking spaces still available in the school.
    """
    # L1
    front_parking_spaces = 52 # 52 parking spaces
    back_parking_spaces = 38 # 38 spaces
    total_parking_spaces = front_parking_spaces + back_parking_spaces

    # L2
    back_spaces_filled_fraction = Fraction(1, 2) # 1/2 of the spaces of the back are filled
    cars_parked_back = back_parking_spaces * back_spaces_filled_fraction

    # L3
    cars_parked_front = 39 # 39 cars have parked
    total_cars_parked = cars_parked_front + cars_parked_back

    # L4
    available_parking_spaces = total_parking_spaces - total_cars_parked

    # FA
    answer = available_parking_spaces
    return answer