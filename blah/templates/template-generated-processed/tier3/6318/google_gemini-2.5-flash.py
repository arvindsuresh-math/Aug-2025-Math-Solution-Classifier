def solve():
    """Index: 6318.
    Returns: the time it will take Celia to run 30 miles.
    """
    # L1
    lexie_time_per_mile = 20 # Lexie 20 minutes to run a mile
    speed_multiplier = 2 # twice as fast
    celia_time_per_mile = lexie_time_per_mile / speed_multiplier

    # L2
    distance_miles = 30 # 30 miles
    total_time_celia = celia_time_per_mile * distance_miles

    # FA
    answer = total_time_celia
    return answer