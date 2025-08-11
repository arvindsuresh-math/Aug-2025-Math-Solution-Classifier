def solve():
    """Index: 2586.
    Returns: the speed of the pilot fish when it moved away from Keanu.
    """
    # L1
    keanu_speed = 20 # speed of 20 miles per hour
    shark_speed_multiplier = 2 # doubled its speed
    shark_new_speed = shark_speed_multiplier * keanu_speed

    # L2
    shark_speed_increase = shark_new_speed - keanu_speed

    # L3
    half_divisor = 2 # half as much as the shark had increased its speed by
    pilot_fish_speed_increase = shark_speed_increase / half_divisor

    # L4
    pilot_fish_final_speed = keanu_speed + pilot_fish_speed_increase

    # FA
    answer = pilot_fish_final_speed
    return answer