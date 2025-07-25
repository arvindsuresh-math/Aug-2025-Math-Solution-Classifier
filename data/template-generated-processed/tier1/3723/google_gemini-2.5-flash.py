def solve():
    """Index: 3723.
    Returns: the time it will take Chase to travel from Granville to Salisbury in minutes.
    """
    # L1
    danielle_travel_time = 30 # 30 minutes to travel from Granville to Salisbury
    danielle_speed_multiplier = 3 # three times the speed of Cameron
    cameron_travel_time = danielle_travel_time * danielle_speed_multiplier

    # L2
    cameron_speed_multiplier = 2 # twice the speed of his brother, Chase
    chase_travel_time = cameron_travel_time * cameron_speed_multiplier

    # FA
    answer = chase_travel_time
    return answer