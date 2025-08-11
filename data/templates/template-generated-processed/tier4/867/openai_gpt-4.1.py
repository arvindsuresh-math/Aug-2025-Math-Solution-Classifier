def solve():
    """Index: 867.
    Returns: the number of minutes before Jim catches Bob.
    """
    # L1
    bob_speed_mph = 6 # Bob runs 6 miles per hour
    minutes_per_hour = 60 # WK
    bob_speed_mpm = bob_speed_mph / minutes_per_hour

    # L2
    jim_speed_mph = 9 # Jim runs at 9 miles per hour
    jim_speed_mpm = jim_speed_mph / minutes_per_hour

    # L4
    head_start = 1 # Bob has a 1 mile head-start
    speed_difference = jim_speed_mpm - bob_speed_mpm

    # L5
    minutes_to_catch = head_start / speed_difference

    # FA
    answer = minutes_to_catch
    return answer