def solve():
    """Index: 3503.
    Returns: the number of minutes longer it would take Derek to walk 20 miles with his brother.
    """
    # L1
    derek_time_alone_per_mile = 9 # 9 minutes to walk a mile if he doesn't have to walk with his brother
    distance_miles = 20 # walk 20 miles
    time_alone_total = derek_time_alone_per_mile * distance_miles

    # L2
    derek_time_with_brother_per_mile = 12 # 12 minutes to walk a mile
    time_with_brother_total = derek_time_with_brother_per_mile * distance_miles

    # L3
    minutes_longer = time_with_brother_total - time_alone_total

    # FA
    answer = minutes_longer
    return answer