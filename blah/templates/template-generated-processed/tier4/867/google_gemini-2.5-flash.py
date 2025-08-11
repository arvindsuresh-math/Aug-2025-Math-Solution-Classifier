def solve():
    """Index: 867.
    Returns: the number of minutes it will take before Jim catches Bob.
    """
    # L1
    bob_speed_mph = 6 # Bob runs 6 miles per hour
    minutes_per_hour = 60 # WK
    bob_speed_mpm = bob_speed_mph / minutes_per_hour

    # L2
    jim_speed_mph = 9 # Jim runs at 9 miles per hour
    jim_speed_mpm = jim_speed_mph / minutes_per_hour

    # L4
    bob_head_start_miles = 1 # Bob has a 1 mile head-start
    relative_speed_mpm = jim_speed_mpm - bob_speed_mpm

    # L5
    time_to_catch_minutes = bob_head_start_miles / relative_speed_mpm

    # FA
    answer = time_to_catch_minutes
    return answer