def solve():
    """Index: 1990.
    Returns: the year that the third car was made.
    """
    # L1
    first_car_year = 1970 # The first car, made in 1970
    years_earlier = 10 # 10 years earlier than the second car
    second_car_year = first_car_year + years_earlier

    # L2
    years_later = 20 # 20 years later after the second car
    third_car_year = second_car_year + years_later

    # FA
    answer = third_car_year
    return answer