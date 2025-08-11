def solve():
    """Index: 2940.
    Returns: the total hours Chrystal will spend to pass the whole mountain.
    """
    # L1
    base_speed = 30 # Chrystal’s vehicle speed is 30 miles per hour
    ascend_decrease_fraction = 0.50 # speed decreases by fifty percent
    ascend_speed = base_speed * ascend_decrease_fraction

    # L2
    ascend_distance = 60 # distance going to the top of the mountain is 60 miles
    ascend_time = ascend_distance / ascend_speed

    # L3
    descend_increase_fraction = 0.20 # speed increases by twenty percent
    descend_speed_increase = base_speed * descend_increase_fraction

    # L4
    descend_speed = base_speed + descend_speed_increase

    # L5
    descend_distance = 72 # distance going down to the foot of the mountain is 72 miles
    descend_time = descend_distance / descend_speed

    # L6
    total_time = ascend_time + descend_time

    # FA
    answer = total_time
    return answer