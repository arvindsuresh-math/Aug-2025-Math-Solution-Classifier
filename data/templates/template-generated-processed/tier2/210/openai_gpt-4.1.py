def solve():
    """Index: 210.
    Returns: the number of toy cars Bobby will have in three years.
    """
    # L1
    initial_cars = 16 # Bobby has 16 toy cars
    percent_increase = 0.5 # increases by 50% every year
    first_year_new_cars = initial_cars * percent_increase

    # L2
    after_first_year = initial_cars + first_year_new_cars

    # L3
    second_year_new_cars = after_first_year * percent_increase

    # L4
    after_second_year = after_first_year + second_year_new_cars

    # L5
    third_year_new_cars = after_second_year * percent_increase

    # L6
    after_third_year = after_second_year + third_year_new_cars

    # FA
    answer = after_third_year
    return answer