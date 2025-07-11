def solve():
    """Index: 2435.
    Returns: Frank's age in 5 years.
    """
    # L1
    karen_age = 2 # Karen is currently 2 years old
    carla_older_than_karen = 2 # Carla is currently 2 years older than Karen
    carla_age = karen_age + carla_older_than_karen

    # L2
    ty_times_carla = 2 # two times as old as Carla
    ty_more_than_twice_carla = 4 # 4 years more than two times as old as Carla
    ty_age = (ty_times_carla * carla_age) + ty_more_than_twice_carla

    # L3
    frank_multiplier = 3 # three times as old as Ty is now
    frank_in_5_years = ty_age * frank_multiplier

    # FA
    answer = frank_in_5_years
    return answer