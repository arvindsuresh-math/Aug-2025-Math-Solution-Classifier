def solve():
    """Index: 4415.
    Returns: the total inches of water the gauge will contain at 9pm.
    """
    # L1
    start_time_phase1 = 2 # From 2pm
    end_time_phase1 = 4 # to 4pm
    duration_phase1 = end_time_phase1 - start_time_phase1

    # L2
    rate_phase1 = 4 # at a rate of 4 inches per hour
    added_rain_phase1 = duration_phase1 * rate_phase1

    # L3
    start_time_phase2 = 4 # From 4pm
    end_time_phase2 = 7 # to 7pm
    duration_phase2 = end_time_phase2 - start_time_phase2

    # L4
    rate_phase2 = 3 # at a rate of 3 inches per hour
    added_rain_phase2 = duration_phase2 * rate_phase2

    # L5
    start_time_phase3 = 7 # From 7pm
    end_time_phase3 = 9 # to 9pm
    duration_phase3 = end_time_phase3 - start_time_phase3

    # L6
    rate_phase3 = 0.5 # at a rate of 0.5 inches per hour
    added_rain_phase3 = duration_phase3 * rate_phase3

    # L7
    initial_rain_gauge_level = 2 # already containing 2 inches of rainwater
    final_rain_gauge_level = initial_rain_gauge_level + added_rain_phase1 + added_rain_phase2 + added_rain_phase3

    # FA
    answer = final_rain_gauge_level
    return answer