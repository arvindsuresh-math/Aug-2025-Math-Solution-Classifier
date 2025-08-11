def solve():
    """Index: 210.
    Returns: the total number of toy cars Bobby will have in three years.
    """
    # L1
    initial_cars = 16 # Bobby has 16 toy cars
    increase_rate_decimal = 0.5 # increases by 50%
    new_cars_year1 = initial_cars * increase_rate_decimal

    # L2
    total_cars_year1 = initial_cars + new_cars_year1

    # L3
    new_cars_year2 = total_cars_year1 * increase_rate_decimal

    # L4
    total_cars_year2 = total_cars_year1 + new_cars_year2

    # L5
    new_cars_year3 = total_cars_year2 * increase_rate_decimal

    # L6
    total_cars_year3 = total_cars_year2 + new_cars_year3

    # FA
    answer = total_cars_year3
    return answer