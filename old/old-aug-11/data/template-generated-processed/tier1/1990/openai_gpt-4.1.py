def solve():
    """Index: 1990.
    Returns: the year the third car was made.
    """
    # L1
    first_car_year = 1970 # The first car, made in 1970
    diff_first_second = 10 # made 10 years earlier than the second car
    second_car_year = first_car_year + diff_first_second

    # L2
    diff_second_third = 20 # third car was manufactured 20 years later after the second car
    third_car_year = second_car_year + diff_second_third

    # FA
    answer = third_car_year
    return answer