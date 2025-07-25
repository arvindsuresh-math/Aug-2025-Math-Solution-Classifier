def solve():
    """Index: 1875.
    Returns: the time in hours for the rabbit to catch up to the cat.
    """
    # L1
    head_start_minutes = 15 # 15-minute head start
    minutes_per_hour = 60 # WK
    head_start_hours = head_start_minutes / minutes_per_hour

    # L2
    cat_speed = 20 # His cat can run 20 miles per hour
    cat_head_start_distance = cat_speed * head_start_hours

    # L3
    rabbit_speed = 25 # Tom's rabbit can run at 25 miles per hour
    speed_difference = rabbit_speed - cat_speed

    # L4
    time_to_catch_up = cat_head_start_distance / speed_difference

    # FA
    answer = time_to_catch_up
    return answer