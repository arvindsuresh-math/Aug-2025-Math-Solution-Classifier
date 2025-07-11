def solve():
    """Index: 1419.
    Returns: the number of kilometers Arvin ran on the 5th day.
    """
    # L1
    first_day_distance = 2 # On the first day, he ran 2 kilometers
    daily_increase = 1 # increased his running distance by 1 kilometer over the previous day
    second_day_distance = first_day_distance + daily_increase

    # L2
    third_day_distance = second_day_distance + daily_increase

    # L3
    fourth_day_distance = third_day_distance + daily_increase

    # L4
    fifth_day_distance = fourth_day_distance + daily_increase

    # FA
    answer = fifth_day_distance
    return answer