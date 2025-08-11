def solve():
    """Index: 6307.
    Returns: the duration of the TV show itself, not counting commercials, in hours.
    """
    # L1
    commercial_duration_minutes = 10 # lasted 10 minutes each
    num_commercials = 3 # 3 commercials
    total_commercial_duration_minutes = num_commercials * commercial_duration_minutes

    # L2
    total_aired_time_hours = 1.5 # aired for 1.5 hours
    commercial_duration_in_hours_for_calc = 0.5 # from solution text: 0.5 of an hour
    actual_show_duration_hours = total_aired_time_hours - commercial_duration_in_hours_for_calc

    # FA
    answer = actual_show_duration_hours
    return answer