def solve():
    """Index: 1170.
    Returns: the number of minutes Andy will be late to school.
    """
    # L1
    school_start_hour = 8 # School starts at 8:00 AM
    school_start_minute = 0 # School starts at 8:00 AM
    leave_hour = 7 # he left his house at 7:15
    leave_minute = 15 # he left his house at 7:15
    school_start_total_minutes = school_start_hour * 60 + school_start_minute
    leave_total_minutes = leave_hour * 60 + leave_minute
    time_available = school_start_total_minutes - leave_total_minutes

    # L2
    red_light_wait = 3 # 3 minutes each at 4 red lights
    num_red_lights = 4 # 4 red lights
    total_red_light_time = red_light_wait * num_red_lights

    # L3
    normal_travel_time = 30 # it normally takes him 30 minutes
    construction_wait = 10 # wait 10 minutes to get past construction
    total_travel_time = normal_travel_time + total_red_light_time + construction_wait

    # L4
    minutes_late = total_travel_time - time_available

    # FA
    answer = minutes_late
    return answer