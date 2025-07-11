def solve():
    """Index: 1468.
    Returns: how much farther Emily walks to school and back in five days.
    """
    # L1
    troy_distance_to_school = 75 # Troy's home is 75 meters away from school
    round_trip_multiplier = 2 # WK
    troy_daily_walk = troy_distance_to_school * round_trip_multiplier

    # L2
    emily_distance_to_school = 98 # Emily's home is 98 meters away from school
    emily_daily_walk = emily_distance_to_school * round_trip_multiplier

    # L3
    daily_difference = emily_daily_walk - troy_daily_walk

    # L4
    num_days = 5 # in five days
    total_difference_five_days = daily_difference * num_days

    # FA
    answer = total_difference_five_days
    return answer