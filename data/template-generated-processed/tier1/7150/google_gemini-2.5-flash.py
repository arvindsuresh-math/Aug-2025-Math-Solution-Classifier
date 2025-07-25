def solve():
    """Index: 7150.
    Returns: the total number of cars owned by all of them.
    """
    # L1
    lindsey_more_than_cathy = 4 # 4 more cars than Cathy
    cathy_cars = 5 # Cathy owns 5 cars
    lindsey_cars = lindsey_more_than_cathy + cathy_cars

    # L2
    multiplier_for_carol = 2 # twice as many cars as Cathy
    carol_cars = multiplier_for_carol * cathy_cars

    # L3
    susan_fewer_than_carol = 2 # 2 fewer cars than Carol
    susan_cars = carol_cars - susan_fewer_than_carol

    # L4
    total_cars = cathy_cars + lindsey_cars + carol_cars + susan_cars

    # FA
    answer = total_cars
    return answer