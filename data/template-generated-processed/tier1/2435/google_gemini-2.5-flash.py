def solve():
    """Index: 2435.
    Returns: Frank's age in 5 years.
    """
    # L1
    karen_current_age = 2 # Karen is currently 2 years old
    carla_older_than_karen = 2 # Carla is currently 2 years older than Karen
    carla_current_age = karen_current_age + carla_older_than_karen

    # L2
    ty_multiplier = 2 # two times as old as Carla
    ty_more_than_twice_carla = 4 # 4 years more than two times as old as Carla
    ty_current_age = (ty_multiplier * carla_current_age) + ty_more_than_twice_carla

    # L3
    frank_multiplier = 3 # three times as old as Ty is now
    frank_age_in_5_years = ty_current_age * frank_multiplier

    # FA
    answer = frank_age_in_5_years
    return answer