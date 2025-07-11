def solve():
    """Index: 1468.
    Returns: how much farther Emily walks to school and back in five days than Troy.
    """
    # L1
    troy_home_to_school = 75 # Troy's home is 75 meters away from school
    trips_per_day = 2 # to school and back home
    troy_daily_distance = troy_home_to_school * trips_per_day

    # L2
    emily_home_to_school = 98 # Emily's home is 98 meters away from school
    emily_daily_distance = emily_home_to_school * trips_per_day

    # L3
    emily_extra_per_day = emily_daily_distance - troy_daily_distance

    # L4
    num_days = 5 # in five days
    emily_extra_total = emily_extra_per_day * num_days

    # FA
    answer = emily_extra_total
    return answer