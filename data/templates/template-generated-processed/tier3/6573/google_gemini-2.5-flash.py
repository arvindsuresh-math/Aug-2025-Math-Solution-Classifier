def solve():
    """Index: 6573.
    Returns: the total time in minutes for the candy to be done.
    """
    # L1
    target_heat_temp = 240 # to 240 degrees
    initial_temp = 60 # from 60 degrees
    degrees_to_heat = target_heat_temp - initial_temp

    # L2
    heat_rate = 5 # heats at 5 degrees/minute
    time_to_heat = degrees_to_heat / heat_rate

    # L3
    target_cool_temp = 170 # cool it down to 170 degrees
    degrees_to_cool = target_heat_temp - target_cool_temp

    # L4
    cool_rate = 7 # cools at 7 degrees/minute
    time_to_cool = degrees_to_cool / cool_rate

    # L5
    total_time = time_to_cool + time_to_heat

    # FA
    answer = total_time
    return answer