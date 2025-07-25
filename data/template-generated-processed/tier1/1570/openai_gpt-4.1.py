def solve():
    """Index: 1570.
    Returns: the number of ounces of chocolate milk Holly began the day with.
    """
    # L1
    end_of_day_ounces = 56 # she ends the day with 56 ounces
    dinner_ounces = 8 # drinks another 8 ounces with dinner
    before_dinner = end_of_day_ounces + dinner_ounces

    # L2
    lunch_ounces = 8 # drinks 8 ounces during lunch
    before_lunch = before_dinner + lunch_ounces

    # L3
    bought_ounces = 64 # buys a new 64-ounce container
    before_buying = before_lunch - bought_ounces

    # L4
    breakfast_ounces = 8 # drinks 8 ounces with breakfast
    start_of_day = before_buying + breakfast_ounces

    # FA
    answer = start_of_day
    return answer